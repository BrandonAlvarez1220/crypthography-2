from Crypto.Util import number
import random
import sympy


class DHKE:

    def __init__(self):

    #Test numbers p:11 and g:2
        self.p = 11  #number.getPrime(1024)
        self.g = self.findGenerator(self.p)

        print(f"Numero primo p generado: {self.p}")
        print(f"Generador g: {self.g}")

    def findGenerator(self, p):
        # Factoriza p - 1
        factors = sympy.factorint(p - 1)
        attempts = 0
        max_attempts = 5  # Limitar el número de intentos
        while attempts < max_attempts:
            g = random.randint(2, p - 2)
            is_generator = all(pow(g, (p - 1) // q, p) != 1 for q in factors)
            if is_generator:
                return g
            attempts += 1
        raise ValueError("No se pudo encontrar un generador después de muchos intentos.")

    def generateRandomKey(self):
        return random.randint(2, self.p - 1)
    def computePublicKey(self, key):
        return pow(self.g, key, self.p)

    def computePrivateKey(self, recivedKey, privateKey):
        return pow(recivedKey, privateKey, self.p)


bob = DHKE()
alice = DHKE()

A = alice.computePublicKey(5)
B = bob.computePublicKey(7)

print(f"A: {A}")
print(f'B: {B}')

CA = alice.computePrivateKey(B, 5)
CB = bob.computePrivateKey(A, 7)

print(f' CA: {CA} & CB: {CB} por lo tanto {CA} = {CB}')