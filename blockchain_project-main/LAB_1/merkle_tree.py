# merkle_tree.py
from custom_hash import custom_hash

def calculate_merkle_root(transaction_hashes):
    if not transaction_hashes:  # Егер тізім бос болса
        return "0"  # Немесе басқа да бастапқы мәндер
    while len(transaction_hashes) > 1:
        temp_hashes = []
        for i in range(0, len(transaction_hashes), 2):
            if i + 1 < len(transaction_hashes):
                temp_hashes.append(custom_hash(transaction_hashes[i] + transaction_hashes[i + 1]))
            else:
                temp_hashes.append(transaction_hashes[i])  # Егер соңғы жұп болса
        transaction_hashes = temp_hashes
    return transaction_hashes[0]
