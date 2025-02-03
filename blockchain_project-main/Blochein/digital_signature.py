import rsa

def sign_data(data, private_key):
    return rsa.sign(data.encode(), private_key, 'SHA-256')

def verify_signature(data, signature, public_key):
    try:
        rsa.verify(data.encode(), signature, public_key)
        return True
    except:
        return False
