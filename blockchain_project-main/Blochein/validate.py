from digital_signature import verify_signature

def validate_transaction(transaction, signature, public_key):
    return verify_signature(transaction, signature, public_key)
