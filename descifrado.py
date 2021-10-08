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
    with open('cifrado_documento','rb') as c_files:
        iv = c_files.read(16)
        descifrado= c_files.read()
    cipher= AES.new(key,AES.MODE_ECB,iv)
    cifrado = unpad(cipher.decrypt(descifrado),AES.block_size)
