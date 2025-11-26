
abc = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z' ]

def cifrado_cesar(data,m_v):
    # cifrar = input("Mensaje a cifrar: ")
    # moving_value = int(input("Numero del cifrado cesar: "))
    cifrar = data
    moving_value = int(m_v)
    
    list_c = list(cifrar)
    cifrado = ""
    
    for c in list_c:
        if c in abc:
            index = abc.index(c)
            x = index + moving_value
            if x >= 52:
                m = x - 52
                a = abc[m]
            else:
                a = abc[x]
            cifrado += a
    return cifrado

def descifrado_de_cesar(data,m_v):
    # descifrado = input("inserte el mensaje cifrado: ")
    # dm_v = int(input("Numero del cifrado cesar: "))
    descifrado = data
    dm_v = int(m_v)
    
    list_d = list(descifrado)
    des = ""
    
    for i in list_d:
        if i in abc:
            index = abc.index(i)
            x = index - dm_v
            if x >= 52:
                m = x - 52
                a = abc[m]
            else:
                a = abc[x]
            des += a
    return des

# a = cifrado_cesar()
# print(a)
# b = descifrado_de_cesar()
# print(b)