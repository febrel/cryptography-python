from cryptography.fernet import Fernet

def decrypt():
    # Abre el archivo la key y la clave
    key = open('pass.key', 'rb').read()
    clave = Fernet(key)
    pass_enc = (open('pass.enc', 'rb').read())
    password = clave.decrypt((pass_enc)).decode('utf-8') # utf-8
    
    return password

print(decrypt())