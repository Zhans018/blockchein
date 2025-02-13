from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Блокчейннің негізгі құрылымы
class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='1', proof=100)

    def create_block(self, proof, previous_hash):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': '2025-02-13',
            'proof': proof,
            'previous_hash': previous_hash,
        }
        self.chain.append(block)
        return block

# Блокчейн объектісін жасаймыз
blockchain = Blockchain()

@app.route('/get_chain', methods=['GET'])
def get_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

@app.route('/mine', methods=['GET'])
def mine():
    last_block = blockchain.chain[-1]
    last_proof = last_block['proof']
    proof = last_proof + 1  # Нақты есептеу логикасын қосыңыз
    previous_hash = last_block['previous_hash']
    block = blockchain.create_block(proof, previous_hash)
    response = {
        'message': 'New Block Mined',
        'index': block['index'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
