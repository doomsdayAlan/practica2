import sys
from Crypto.Cipher import AES # Importamos el módulo RSA
from Crypto.Util.Padding import pad
print ("Ingrese que tipo de cifrdo va a usar")
tipoCifrado = input()
if tipoCifrado == 'CBC':
    key= b'holamundocomoest'
    cipher= AES.new(key,AES.MODE_CBC)
    plaintext = b'me gusta jugar con las patas'
    cifrado = cipher.encrypt(pad(plaintext,AES.block_size))
    print(cifrado)
    with open('cifrado_MODE_CBC','wb') as c_files:
        c_files.write(cipher.iv)
        c_files.write(cifrado)

elif tipoCifrado == 'ECB':
    key= b'holamundocomoest'
    cipherr= AES.new(key,AES.MODE_ECB)
    plaintext = b'me gusta jugar con las patas'
    cifrado = cipherr.encrypt(pad(plaintext,AES.block_size))
    print(cifrado)
    with open('cifrado_MODE_ECB','wb') as c_files:
        c_files.write(cipherr.iv)
        c_files.write(cifrado)

elif tipoCifrado == 'CFB':
    key= b'holamundocomoest'
    cipher= AES.new(key,AES.MODE_CFB)
    plaintext = b'me gusta jugar con las patas'
    cifrado = cipher.encrypt(pad(plaintext,AES.block_size))
    print(cifrado)
    with open('cifrado_MODE_CFB','wb') as c_files:
        c_files.write(cipher.iv)
        c_files.write(cifrado)

elif tipoCifrado == 'OFB':
    key= b'holamundocomoest'
    cipher= AES.new(key,AES.MODE_OFB)
    plaintext = b'me gusta jugar con las patas'
    cifrado = cipher.encrypt(pad(plaintext,AES.block_size))
    print(cifrado)
    with open('cifrado_AES.MODE_OFB','wb') as c_files:
        c_files.write(cipher.iv)
        c_files.write(cifrado)
else:
    print('no exite ese cifrado')
