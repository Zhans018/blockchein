# block_explorer_gui.py
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
            block_info = f"Блок {i}\nХэш: {block.hash}\nВремя: {block.timestamp}\nДанные: {block.data}\nМеркле түбірі: {block.merkle_root}"
            label = tk.Label(
                self.root,
                text=block_info,
                relief="solid",
                borderwidth=2,
                padx=10,
                pady=10,
            )
            label.pack(pady=5)

    def run(self):
        self.root.mainloop()
