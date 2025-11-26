from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

def cryptografy(data):
        # mensaje = input("Elige tu mensaje a cifrar: ")
        mensaje = data
        mensaje = bytes(mensaje, "utf-8")
        mensaje_cifrado = f.encrypt(mensaje)
        return mensaje_cifrado, key

def decryptografy(data, key):
        # mensaje_ds = input("Elige tu mensaje a descifrar: ")
        mensaje_ds = data
        mensaje_ds = bytes(mensaje_ds, 'utf-8')
        # llave = bytes(input("inserte clave entregada: "),'utf-32')
        llave = bytes(key,'utf-32')
        k = Fernet(llave)
        mensaje_descifrado = k.decrypt(mensaje_ds)
        mensaje_original = mensaje_descifrado.decode('utf-8')
        return mensaje_original
    