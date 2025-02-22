import time
from merkle_tree import calculate_merkle_root
from custom_hash import custom_hash
import hashlib

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.merkle_root = self.calculate_merkle_root()  # 🔥 Жаңадан қостық!
        self.hash = self.calculate_hash()

    def calculate_merkle_root(self):
        """Merkle Root есептеу (қазіргі нұсқада қарапайым Hash)"""
        if not self.data:
            return hashlib.sha256(b"").hexdigest()
        
        combined_data = "".join(str(tx) for tx in self.data)
        return hashlib.sha256(combined_data.encode()).hexdigest()

    def calculate_hash(self):
        """Блоктың хешін есептеу"""
        data_string = f"{self.timestamp}{self.data}{self.previous_hash}{self.merkle_root}"
        return hashlib.sha256(data_string.encode()).hexdigest()

    def to_dict(self):  # ✅ JSON форматында шығару үшін
        return {
            "timestamp": self.timestamp,
            "data": self.data,
            "previous_hash": self.previous_hash,
            "merkle_root": self.merkle_root,
            "hash": self.hash
        }
