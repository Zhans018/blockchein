from flask import Flask, request, jsonify
import requests
import hashlib
import json
import time
from blockchain import Blockchain

app = Flask(__name__)

blockchain = Blockchain()
transactions = []
peers = set()

def create_block(proof, previous_hash):
    blockchain.add_block({
        'transactions': transactions.copy(),
        'proof': proof,
    })
    transactions.clear()
    return blockchain.chain[-1]

@app.route('/mine', methods=['GET'])
def mine_block():
    last_block = blockchain.chain[-1]
    new_proof = proof_of_work(last_block.hash)
    
    block = create_block(new_proof, last_block.hash)

    response = {'message': 'Жаңа блок өндірілді', 'block': block.to_dict()}
    return jsonify(response), 200

@app.route('/chain', methods=['GET'])
def get_chain():
    return jsonify({'chain': [block.to_dict() for block in blockchain.chain]}), 200

@app.route('/transaction', methods=['POST'])
def add_transaction():
    tx_data = request.get_json()
    transactions.append(tx_data)
    return jsonify({'message': 'Транзакция қосылды'}), 201

@app.route('/blocks', methods=['GET'])
def get_blocks():
    return jsonify({"chain": [block.to_dict() for block in blockchain.chain]}), 200

def proof_of_work(last_proof):
    proof = 0
    while not is_valid_proof(last_proof, proof):
        proof += 1
    return proof

def is_valid_proof(last_proof, proof):
    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == '0000'

if __name__ == '__main__':
    app.run(port=5000)
