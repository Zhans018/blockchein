import requests

node_url = "http://127.0.0.1:5000"

def mine_block():
    response = requests.get(f"{node_url}/mine")
    return response.json()

if __name__ == "__main__":
    print(mine_block())
