# gui.py
import tkinter as tk
from blockchain import Blockchain

class BlockExplorerGUI:
    def __init__(self, blockchain):
        self.blockchain = blockchain
        self.root = tk.Tk()
        self.root.title("Блокчейн Эксплорер")
        self.create_ui()

    def create_ui(self):
        for i, block in enumerate(self.blockchain.chain):
            for tx in block.transactions:
                tx_info = f"Жіберуші: {tx.sender}, Алушы: {tx.receiver}, Сома: {tx.amount}, Комиссия: {tx.fee}, Адрес: {tx.transaction_hash}"
                label = tk.Label(self.root, text=tx_info, relief="solid", borderwidth=2, padx=10, pady=10)
                label.pack(pady=5)

    def run(self):
        self.root.mainloop()
