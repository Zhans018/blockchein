import requests

# Блокчейн серверіне сұраныс жасау
def get_blockchain():
    url = 'http://127.0.0.1:5000/get_chain'
    response = requests.get(url)
    if response.status_code == 200:
        blockchain = response.json()
        return blockchain
    else:
        return None

# Блокчейнді көрсету
blockchain = get_blockchain()
if blockchain:
    print("Blockchain:")
    for block in blockchain['chain']:
        print(f"Block {block['index']} - Proof: {block['proof']}")
else:
    print("Blockchain could not be retrieved.")
