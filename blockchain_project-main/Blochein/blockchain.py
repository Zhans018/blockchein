import time
import hashlib
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = []  # Блоктардың тізбегі
        self.pending_transactions = []  # Күтіп тұрған транзакциялар
        self.mining_reward = 10  # Минерлерге берілетін жүлде
        self.create_genesis_block()  # Генезис блогын жасау

    def create_genesis_block(self):
        """ Генезис блогын жасайды (блокчейннің бірінші блогы) """
        genesis_block = Block(time.time(), ["Genesis Block"], "0")
        self.chain.append(genesis_block)  # Генезис блогын тізбекке қосамыз

    def mine_pending_transactions(self, miner_address):
        """ Күтіп тұрған транзакцияларды өңдеу """
        # Минерге жүлде ретінде жаңа транзакция қосамыз
        reward_transaction = {"sender": "Blockchain", "receiver": miner_address, "amount": self.mining_reward}
        self.pending_transactions.append(reward_transaction)

        # Жаңа блок жасау және оны тізбекке қосу
        new_block = Block(len(self.chain), self.pending_transactions, self.chain[-1].hash)
        self.chain.append(new_block)

        # Күтіп тұрған транзакцияларды тазалау
        self.pending_transactions = []

    def add_block(self, data):
        """ Жаңа блок қосу """
        previous_hash = self.chain[-1].hash if self.chain else "0"
        timestamp = time.time()  # Уақыт белгісін қосу
    
        block = Block(data=data, previous_hash=previous_hash, timestamp=timestamp)
        self.chain.append(block)  # Блокты тізбекке қосу
        return block

    def is_chain_valid(self):
        """ Блокчейннің жарамдылығын тексереді """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Хэштерді салыстыру
            if current.hash != current.calculate_hash():
                print(f"⚠️ Қате: {i}-блоктың хэші дұрыс емес!")
                return False

            # Алдыңғы блоктың хэшін тексеру
            if current.previous_hash != previous.hash:
                print(f"⚠️ Қате: {i}-блоктың алдыңғы хэші сәйкес келмейді!")
                return False

        print("✅ Блокчейн жарамды!")
        return True
