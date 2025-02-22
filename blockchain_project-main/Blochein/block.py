import time
from merkle_tree import calculate_merkle_root
from custom_hash import custom_hash

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.merkle_root = self.calculate_merkle_root()
        self.hash = self.calculate_hash()

    def calculate_merkle_root(self):
        transaction_hashes = [custom_hash(transaction) for transaction in self.data]
        return calculate_merkle_root(transaction_hashes)

    def calculate_hash(self):
        return custom_hash(f"{self.timestamp}{self.data}{self.previous_hash}{self.merkle_root}")

    def to_dict(self):  # ✅ JSON форматында шығару үшін
        return {
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "merkle_root": self.merkle_root,
            "hash": self.hash
        }
