import math
import random

Primes = ["2", "3", "5", "7", "11", "13", "17", "19", "23",
          "29", "31", "37", "41", "43", "47", "53","59",
          "61", "67", "71", "73", "79", "83", "89", "97"]
dicc = {}

def rsa_e(data, key):
    p = random.choice(Primes)
    p = int(p)
    q = random.choice(Primes)
    q = int(q)
    n = p*q
    phi = (p-1)*(q-1)
    e = 2

    while e<phi:
        if (math.gcd(e,phi)==1):
            break
        else:
            e += 1

    d = pow(e,-1,phi)
    # text = input("Mensaje que quieres encriptar: ")
    # msg = int(input("Elija su clave: "))
    text = data
    msg = int(key)

    C = pow(msg,e,n)
    M = pow(C, d, n)
        
    dicc["save"] = text
    dicc["s_k"] = M
    dicc["enc"] = C
        
    return C,M
       
def rsa_d(data,k):
    # cry = int(input("Mensaje encriptado: "))
    # key = int(input("Inserte clave: "))
    cry = data
    key = k
    if dicc.get("enc") == cry and dicc.get("s_k") == key:
        return dicc.get("save")
    else:
        str = "la clave o el mensaje encriptado fue incorrecto"
        return str
        
