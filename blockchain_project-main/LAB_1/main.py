# main.py
from blockchain import Blockchain
from block_explorer_gui import BlockExplorerGUI

# Блокчейнді құру
blockchain = Blockchain()

# Жаңа блоктарды қосу
blockchain.add_block(["Данные 1"])
blockchain.add_block(["Данные 2"])

# Блоктарды графикалық интерфейсте көрсету
app = BlockExplorerGUI(blockchain)
app.run()
