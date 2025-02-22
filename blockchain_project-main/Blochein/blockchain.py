import time
from block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        """ Генезис блогын жасайды (блокчейннің бірінші блогы) """
        return Block(time.time(), ["Genesis Block"], "0")

    def add_block(self, data):
        previous_hash = self.chain[-1].hash if self.chain else "0"
        timestamp = time.time()  # 🔥 Уақыт белгісін қосамыз!
    
        block = Block(data=data, previous_hash=previous_hash, timestamp=timestamp)
        self.chain.append(block)
        return block

    def is_chain_valid(self):
        """ Блокчейннің жарамдылығын тексереді """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                print(f"⚠️ Қате: {i}-блоктың хэші дұрыс емес!")
                return False

            if current.previous_hash != previous.hash:
                print(f"⚠️ Қате: {i}-блоктың алдыңғы хэші сәйкес келмейді!")
                return False

        print("✅ Блокчейн жарамды!")
        return True
