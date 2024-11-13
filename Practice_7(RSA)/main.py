
from RSA import RSA

rsa = RSA()

rsa.key_generation()

password = rsa.password_generator()

print(f"La contraseña es:{password}")

cipher_password = rsa.cipher("PublicKey.txt", password)

print(f'La contraseña cifrada es: {cipher_password}')

#Decifrado
decipher_password = rsa.decipher('PrivateKey.txt', ciphertext=cipher_password)

print(f'La contraseña decifrada es:{decipher_password}')
