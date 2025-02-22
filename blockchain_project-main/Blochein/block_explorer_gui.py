import tkinter as tk
import requests

NODE_URL = "http://127.0.0.1:5000"

class BlockExplorerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Блокчейн Эксплорер")
        self.create_ui()

    def fetch_blocks(self):
        try:
            response = requests.get(f"{NODE_URL}/blocks")
            return response.json().get("chain", [])
        except requests.exceptions.RequestException:
            return []

    def create_ui(self):
        blocks = self.fetch_blocks()
        if not blocks:
            tk.Label(self.root, text="Блоктар табылмады!", fg="red").pack(pady=5)
            return

        for i, block in enumerate(blocks):
            block_info = (
                f"Блок {i}\n"
                f"Хэш: {block['hash']}\n"
                f"Уақыт: {block['timestamp']}\n"
                f"Деректер: {block['data']}\n"
                f"Меркле түбірі: {block['merkle_root']}"
            )
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

if __name__ == "__main__":
    explorer = BlockExplorerGUI()
    explorer.run()
