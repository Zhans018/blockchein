import requests

def mine_block():
    url = 'http://127.0.0.1:5000/mine'
    response = requests.get(url)
    if response.status_code == 200:
        block = response.json()
        print(f"Block {block['index']} mined! Proof: {block['proof']}")
    else:
        print("Mining failed.")

mine_block()
