import time
import json
from block import Block

# Жаңа блок жасау
block = Block(time.time(), ["Transaction 1", "Transaction 2"], "0000")

# Блоктың мәліметтерін JSON форматында әдемі шығару
print(json.dumps(block.to_dict(), indent=4))
