import hashlib
import time

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp  # Блоктың уақыт белгісі
        self.data = data  # Блоктағы деректер (мысалы, транзакциялар)
        self.previous_hash = previous_hash  # Алдыңғы блоктың хэші
        self.hash = self.calculate_hash()  # Блоктың хэші

    def calculate_hash(self):
        """ Блоктың хэшін есептеу """
        block_string = f'{self.timestamp}{self.data}{self.previous_hash}'.encode('utf-8')
        return hashlib.sha256(block_string).hexdigest()

    def to_dict(self):
        """ Блокты дикт түрінде шығару """
        return {
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'hash': self.hash
        }
