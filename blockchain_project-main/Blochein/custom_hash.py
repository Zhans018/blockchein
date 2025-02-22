import hashlib

def custom_hash(data):
    return hashlib.sha256(data.encode()).hexdigest()

# Тест мәндері
print(custom_hash("Blockchain"))
print(custom_hash("Transaction 1"))
print(custom_hash("Transaction 2"))