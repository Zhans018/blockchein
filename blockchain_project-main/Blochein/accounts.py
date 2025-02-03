import hashlib
import rsa

def get_address(public_key):
    return hashlib.sha256(public_key.save_pkcs1()).hexdigest()

if __name__ == "__main__":
    pub_key, priv_key = rsa.newkeys(2048)
    address = get_address(pub_key)
    print(f"Жаңа аккаунт адресі: {address}")
