from Crypto.Util import number
import base64
import random
import string
class RSA:

    def key_generation(self):
        bits = 512
        p = number.getPrime(bits)
        q = number.getPrime(bits)
        n = p * q
        z = (p-1) * (q-1)
        k = 0


        for i in range(2, z-1):

            if number.GCD(z, i) == 1:
                k = i
                break

        j = number.inverse(k, z)

        #Base 64
        n_base64 = base64.b64encode(n.to_bytes((n.bit_length() + 7) // 8, 'big')).decode('utf-8')
        k_base64 = base64.b64encode(k.to_bytes((k.bit_length() + 7) // 8, 'big')).decode('utf-8')
        j_base64 = base64.b64encode(j.to_bytes((j.bit_length() + 7) // 8, 'big')).decode('utf-8')

        #Save in a file text
        private_key = open("PrivateKey.txt", "w").write(j_base64)
        public_key = open("PublicKey.txt", "w").write(n_base64+'\n'+k_base64)

    def cipher(self, publickey, message):

        publickey = open(publickey, "r").readlines()

        m = int.from_bytes(message.encode(), "big")
        n = int.from_bytes(base64.b64decode(publickey[0]), "big")
        k = int.from_bytes(base64.b64decode(publickey[1]), "big")

        C = (m**k) % n

        C_base64 = base64.b64encode(C.to_bytes((C.bit_length() + 7) // 8, 'big')).decode('utf-8')

        return C_base64

    def decipher(self, privatekey, ciphertext):

        privatekey = open(privatekey, "r").readlines()
        publickey = open("PublicKey.txt", "r").readlines()

        j = int.from_bytes(base64.b64decode(privatekey[0]), "big")
        n = int.from_bytes(base64.b64decode(publickey[0]), "big")
        c = int.from_bytes(base64.b64decode(ciphertext), "big")

        M = pow(c, j, n)

        M_decoded = M.to_bytes((M.bit_length() + 7) // 8, 'big').decode('utf-8')

        return M_decoded


    def password_generator(self):
        return ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(7))