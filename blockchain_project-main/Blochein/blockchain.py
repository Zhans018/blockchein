# blockchain.py
import time
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        # Генезис блокқа транзакциялар қосыңыз
        return Block(time.time(), ["Транзакция 1"], "0")

    def add_block(self, data):
        previous_block = self.chain[-1]
        new_block = Block(time.time(), data, previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.calculate_hash():
                return False
            if current.previous_hash != previous.hash:
                return False
        return True
