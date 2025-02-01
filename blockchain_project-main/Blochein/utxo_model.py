# utxo_model.py
class UTXOModel:
    def __init__(self):
        self.utxos = {}  # {"account_address": [list of unspent transaction outputs]}

    def add_transaction(self, transaction):
        # Транзакцияның нәтижесінде пайда болған UTXO-ны қосу
        sender = transaction.sender
        receiver = transaction.receiver
        amount = transaction.amount
        if sender not in self.utxos:
            self.utxos[sender] = []
        self.utxos[sender].append({"amount": -amount, "receiver": receiver})
        if receiver not in self.utxos:
            self.utxos[receiver] = []
        self.utxos[receiver].append({"amount": amount, "sender": sender})

    def get_balance(self, address):
        balance = 0
        if address in self.utxos:
            for utxo in self.utxos[address]:
                balance += utxo["amount"]
        return balance
