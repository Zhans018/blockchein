import tkinter as tk
from tkinter import messagebox
import rsa
import encryption

def create_wallet():
    public_key, private_key = encryption.generate_keys()
    messagebox.showinfo("Wallet", "Әмиян құрылды!")

root = tk.Tk()
root.title("Blockchain Wallet")
tk.Button(root, text="Әмиян құру", command=create_wallet).pack()
root.mainloop()
