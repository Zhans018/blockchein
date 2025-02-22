import tkinter as tk
from tkinter import messagebox
import rsa
import json
import requests
import os

WALLET_FILE = "wallet_keys.json"
NODE_URL = "http://127.0.0.1:5000"

# Кілттерді генерациялау және сақтау
def generate_keys():
    public_key, private_key = rsa.newkeys(512)
    
    # Кілттерді файлға сақтау
    keys = {
        "public_key": public_key.save_pkcs1().decode(),
        "private_key": private_key.save_pkcs1().decode()
    }
    with open(WALLET_FILE, "w") as f:
        json.dump(keys, f)
    
    return public_key, private_key

# Әмиян құру
def create_wallet():
    if os.path.exists(WALLET_FILE):
        messagebox.showinfo("Wallet", "Әмиян бұрыннан бар!")
    else:
        generate_keys()
        messagebox.showinfo("Wallet", "Әмиян құрылды!")

# Әмиянды жүктеу
def load_wallet():
    if os.path.exists(WALLET_FILE):
        with open(WALLET_FILE, "r") as f:
            keys = json.load(f)
            public_key = rsa.PublicKey.load_pkcs1(keys["public_key"].encode())
            private_key = rsa.PrivateKey.load_pkcs1(keys["private_key"].encode())
            return public_key, private_key
    return None, None

# Транзакция жасау
def create_transaction(receiver, amount):
    public_key, private_key = load_wallet()
    if not public_key or not private_key:
        messagebox.showerror("Error", "Әуелі әмиян құрыңыз!")
        return None

    tx_data = {
        "sender": public_key.save_pkcs1().decode(),
        "receiver": receiver,
        "amount": amount
    }
    
    # Қолтаңба жасау
    tx_json = json.dumps(tx_data).encode()
    signature = rsa.sign(tx_json, private_key, 'SHA-256')
    
    return {"transaction": tx_data, "signature": signature.hex()}

# Транзакцияны жіберу
def send_transaction():
    receiver = receiver_entry.get()
    amount = amount_entry.get()
    
    if not receiver or not amount.isdigit():
        messagebox.showerror("Error", "Қабылдаушы және соманы дұрыс енгізіңіз!")
        return

    amount = int(amount)
    transaction = create_transaction(receiver, amount)
    
    if transaction:
        response = requests.post(f"{NODE_URL}/transaction", json=transaction)
        messagebox.showinfo("Transaction", response.json().get("message", "Қате!"))

# Балансты тексеру
def check_balance():
    public_key, _ = load_wallet()
    if not public_key:
        messagebox.showerror("Error", "Әуелі әмиян құрыңыз!")
        return

    response = requests.get(f"{NODE_URL}/balance/{public_key.save_pkcs1().decode()}")
    balance = response.json().get("balance", "Белгісіз")
    
    messagebox.showinfo("Balance", f"Сіздің балансыңыз: {balance} монета")

# --- GUI ---
root = tk.Tk()
root.title("Blockchain Wallet")

tk.Button(root, text="Әмиян құру", command=create_wallet).pack(pady=5)
tk.Button(root, text="Балансты тексеру", command=check_balance).pack(pady=5)

tk.Label(root, text="Қабылдаушының кілті:").pack()
receiver_entry = tk.Entry(root, width=50)
receiver_entry.pack()

tk.Label(root, text="Сома:").pack()
amount_entry = tk.Entry(root, width=20)
amount_entry.pack()

tk.Button(root, text="Транзакция жіберу", command=send_transaction).pack(pady=5)

root.mainloop()
