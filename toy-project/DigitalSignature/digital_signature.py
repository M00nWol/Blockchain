from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, PublicFormat, NoEncryption
from cryptography.exceptions import InvalidSignature

# 개인 키 및 공개 키 저장
def save_keys(private_key, public_key, private_key_path='private_key.pem', public_key_path='public_key.pem'):
    with open(private_key_path, 'wb') as private_file:
        private_file.write(
            private_key.private_bytes(
                encoding=Encoding.PEM,
                format=PrivateFormat.PKCS8,
                encryption_algorithm=NoEncryption()
            )
        )
    
    with open(public_key_path, 'wb') as public_file:
        public_file.write(
            public_key.public_bytes(
                encoding=Encoding.PEM,
                format=PublicFormat.SubjectPublicKeyInfo
            )
        )


# 개인 키 및 공개 키 로드
def load_keys(private_key_path='private_key.pem', public_key_path='public_key.pem'):
    with open(private_key_path, 'rb') as private_file:
        private_key = serialization.load_pem_private_key(private_file.read(), password=None)

    with open(public_key_path, 'rb') as public_file:
        public_key = serialization.load_pem_public_key(public_file.read())

    return private_key, public_key


# 전자서명 생성
def sign_message(private_key, message):
    signature = private_key.sign(
        message, 
        ec.ECDSA(hashes.SHA256())
    )
    return signature


# 전자서명 검증
def verify_signature(public_key, message, signature):
    try:
        public_key.verify(signature, message, ec.ECDSA(hashes.SHA256()))
        return True
    except InvalidSignature:
        return False

# 키 생성
def generate_keys():
    private_key=ec.generate_private_key(ec.SECP256R1)
    public_key=private_key.public_key()
    return private_key, public_key



