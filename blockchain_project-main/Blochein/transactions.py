from digital_signature import sign_data, verify_signature
import rsa

# Кілттерді жүктеу
with open("private.pem", "rb") as priv_file:
    private_key = rsa.PrivateKey.load_pkcs1(priv_file.read())

with open("public.pem", "rb") as pub_file:
    public_key = rsa.PublicKey.load_pkcs1(pub_file.read())

transaction = "Alice -> Bob : 5 BTC"

# Қолтаңбалау
signature = sign_data(transaction, private_key)

# Валидация
is_valid = verify_signature(transaction, signature, public_key)
print(f"✅ Транзакция жарамды ма? {is_valid}")
