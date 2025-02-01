# transaction.py
from custom_hash import custom_hash

class Transaction:
    def __init__(self, sender, recipient, amount, fee):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.fee = fee
        self.transaction_hash = self.calculate_transaction_hash()

    def calculate_transaction_hash(self):
        data = f"{self.sender}{self.recipient}{self.amount}{self.fee}"
        return custom_hash(data)
