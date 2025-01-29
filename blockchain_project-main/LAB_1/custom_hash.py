# custom_hash.py
def custom_hash(data):
    hash_value = 0
    for char in data:
        hash_value += ord(char) ** 2
        hash_value %= 1000000
    return str(hash_value)
