from cryptography.fernet import Fernet

def generar_key():
    key = Fernet.generate_key()
    with open('pass.key', 'wb') as file:
        file.write(key)


def cargar_key():
    return open('pass.key', 'rb').read()


def ecrypt():
    # Llama a las funciones
    generar_key()
    key = cargar_key()

    password = b'EsteMensajeOculto' # Poner Password

    file = open('pass.enc', 'wb')

    # Guarda en un archivo la password
    clave = Fernet(key)
    pass_enc = clave.encrypt(password)
    file.write(pass_enc)
    file.close()

# Llamo la Funcion
ecrypt()