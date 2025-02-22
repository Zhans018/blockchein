import requests

# Блок өндіру
response = requests.post('http://127.0.0.1:5000/mine', json={"data": "Транзакция 1"})
print(response.json())

# Барлық блоктарды көру
response = requests.get('http://127.0.0.1:5000/chain')
print(response.json())

# Блокчейннің дұрыстығын тексеру
response = requests.get('http://127.0.0.1:5000/valid')
print(response.json())
