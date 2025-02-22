from flask import Flask, request, jsonify
import hashlib
import time
from blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()
transactions = []  # Күтіп тұрған транзакциялар

def create_block(proof):
    """ Жаңа блокты жасау және оны блокчейнге қосу """
    last_block = blockchain.chain[-1]  # Соңғы блокты алу
    block_data = {
        'transactions': transactions.copy(),  # Транзакцияларды блокқа қосу
        'proof': proof,
        'previous_hash': last_block.hash  # Алдыңғы блоктың хэші
    }
    
    blockchain.add_block(block_data)  # Блокты тізбекке қосу
    transactions.clear()  # Күтіп тұрған транзакцияларды тазалау
    
    return blockchain.chain[-1]  # Соңғы блокты қайтару

@app.route('/mine', methods=['GET'])
def mine_block():
    """ Жаңа блокты өндіру (Proof of Work қолдану) """
    if not transactions:  # Егер транзакциялар болмаса, блок өндіруге болмайды
        return jsonify({'error': '❌ Миннинг үшін транзакция жоқ!'}), 400

    last_block = blockchain.chain[-1]
    new_proof = proof_of_work(last_block.hash)

    block = create_block(new_proof)

    # Егер `block.data` дұрыс форматта болмаса, оны дұрыстаймыз
    block_transactions = block.data if isinstance(block.data, list) else block.data.get('transactions', [])

    response = {
        'message': '✅ Жаңа блок өндірілді!',
        'block': {
            'transactions': block_transactions,
            'proof': new_proof,
            'previous_hash': block.previous_hash,
            'hash': block.hash
        }
    }
    return jsonify(response), 200

@app.route('/transaction', methods=['POST'])
def add_transaction():
    """ Жаңа транзакцияны қосу """
    tx_data = request.get_json()
    required_fields = ['sender', 'receiver', 'amount']
    
    if not tx_data or not all(k in tx_data for k in required_fields):
        return jsonify({'error': '❌ Қате: Транзакция деректері дұрыс емес!'}), 400

    # Егер `fee` көрсетілмесе, оны 0 деп орнату
    tx_data.setdefault('fee', 0)

    transactions.append(tx_data)
    return jsonify({'message': '✅ Транзакция қосылды!', 'transaction': tx_data}), 201

@app.route('/chain', methods=['GET'])
def get_chain():
    """ Блокчейнді көру """
    return jsonify({'chain': [block.to_dict() for block in blockchain.chain]}), 200

@app.route('/pending_transaction', methods=['GET'])
def get_pending_transactions():
    """ Күтіп тұрған транзакцияларды көру """
    return jsonify({'pending_transactions': transactions}), 200

def proof_of_work(last_hash):
    """ Proof of Work алгоритмі (блокты өндіру) """
    proof = 0
    difficulty = "00000"  # Күрделілікті реттеу (неғұрлым көп 0 болса, соғұрлым қиын)
    
    while not is_valid_proof(last_hash, proof, difficulty):
        proof += 1
    
    return proof

def is_valid_proof(last_hash, proof, difficulty):
    """ Proof of Work-тың дұрыстығын тексеру """
    guess = f'{last_hash}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:len(difficulty)] == difficulty

if __name__ == '__main__':
    app.run(port=5000)
