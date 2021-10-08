import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
print('Que tipo de cifrado vas a descifrar ')
tipoCifrado = input()
if tipoCifrado == 'CBC':
    key= b'holamundocomoest'
    with open('cifrado_MODE_CBC','rb') as c_files:
        iv = c_files.read(16)
        descifrado= c_files.read()
    cipher= AES.new(key,AES.MODE_CBC,iv)
    cifrado = unpad(cipher.decrypt(descifrado),AES.block_size)
    print(cifrado.decode())
elif tipoCifrado == 'ECB':
    key= b'holamundocomoest'
    with open('cifrado_MODE_ECB','rb') as c_files:
        iv = c_files.read(16)
        descifrado= c_files.read()
    cipher= AES.new(key,AES.MODE_ECB,iv)
    cifrado = unpad(cipher.decrypt(descifrado),AES.block_size)
elif tipoCifrado == 'CFB':
    key= b'holamundocomoest'
    with open('cifrado_MODE_CFB','rb') as c_files:
        iv = c_files.read(16)
        descifrado= c_files.read()
    cipher= AES.new(key,AES.MODE_CFB,iv)
    cifrado = unpad(cipher.decrypt(descifrado),AES.block_size)
elif tipoCifrado == 'OFB':
    key= b'holamundocomoest'
    with open('cifrado_AES.MODE_OFB','rb') as c_files:
        iv = c_files.read(16)
        descifrado= c_files.read()
    cipher= AES.new(key,AES.MODE_OFB,iv)
    cifrado = unpad(cipher.decrypt(descifrado),AES.block_size)
else:
    print("no existe ese cifrado")
