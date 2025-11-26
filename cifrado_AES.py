from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

key = get_random_bytes(32)
i = get_random_bytes(16)

# print(f'Recuerda la llave: {key.hex()}')

def encrypt(dt):
    data = bytes(dt, encoding= 'utf-8')
    cif = AES.new(key,AES.MODE_CBC,i)
    pdd = data + b'\0' * (AES.block_size - len(data) % AES.block_size)
    cf_txt = cif.encrypt(pdd)
    print(f'Recuerda la llave: {key.hex()}')
    return cif.iv + cf_txt

def decrypt(ky, data):
    m = bytes.fromhex(data)
    k = bytes.fromhex(ky)
    ii = m[:AES.block_size]
    ncf_txt = m[AES.block_size:]
    cif = AES.new(k,AES.MODE_CBC,ii)
    p_pdd = cif.decrypt(ncf_txt)
    return p_pdd.rstrip(b'\0')


# if x == 1:
#     print(f'mensaje encriptado: {encript.hex()}')
# else:
#     print(f'mensaje encriptado: {encript}')

# m_e = input("mensaje: ")
# m =  bytes.fromhex(m_e)
# k_hx = input("\nIngrese la llave:")
# k = bytes.fromhex(k_hx)

# decript = decrypt(k, m)
# print(f'mensaje desencriptado: {decript}')