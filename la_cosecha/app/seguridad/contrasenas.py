from pwdlib import PasswordHash
from pwdlib.hashers.argon2 import Argon2Hasher
from pwdlib.hashers.bcrypt import BcryptHasher

# Argon2 para las contraseñas nuevas.
# Bcrypt 
# lo para poder verificar contraseñas antiguas que ya estén guardadas en la BD.
pwd_hash = PasswordHash((Argon2Hasher(), BcryptHasher()))


def hashear(password: str) -> str:
    return pwd_hash.hash(password)


def verificar(password: str, password_hash: str) -> bool:
    try:
        return pwd_hash.verify(password, password_hash)
    except Exception:
        return False