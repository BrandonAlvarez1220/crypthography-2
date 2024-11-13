from Crypto.Util import number
import random
import sympy
from sympy import isprime


class DHKE:

    def __init__(self):

        # number.getPrime(1024)
        self.p = 95097084948509115100307292000136748285366004816250451276976287493080952752376091019038776340040185790416069653744291100385743706189695088122638921298221058872148614899587992382882934820894444198312962166612124202781272757307425730013495451419297930668418939581161181450801559423679410128834172850802799447087
        # self.find_generator(self.p)
        self.g = 87374905352644423714357109246086005574397492276389135450142696670539202606373680688702042185829455301971254053059980200759581274166015128746413080228822498991623570598478637136941590197457798991165248622890200751746846789236974908693548748564897676369659708852833403943642565305771571844697629360822161140398

        print(f"Numero primo p generado: {self.p}")
        print(f"Generador g: {self.g}")

    def gcd(self, a, b):
        while b != 0:
            a, b = b, a % b
        return a

    def mod_exp(self, base, exp, mod):
        result = 1
        while exp > 0:
            if exp % 2 == 1:
                result = (result * base) % mod
            base = (base * base) % mod
            exp //= 2
        return result

    # Función para encontrar el generador de un primo grande
    def find_generator(self,p):
        if not isprime(p):
            raise ValueError(f"{p} no es un número primo")

        # En este caso, sólo verificaremos para los dos factores primos más importantes: 2 y (p-1)/2
        q = (p - 1) // 2

        while True:
            g = random.randint(2, p - 2)
            if self.mod_exp(g, 2, p) != 1 and self.mod_exp(g, q, p) != 1:
                return g

    def generateRandomKey(self):
        return random.randint(2, self.p - 1)
    def computePublicKey(self, key):
        return pow(self.g, key, self.p)

    def computePrivateKey(self, recivedKey, privateKey):
        return pow(recivedKey, privateKey, self.p)


alice = DHKE()
#randomkey = alice.generateRandomKey()

randomkey = 66782071163210353119449440991218002334618862794612932468745379354435591374187153702140560159203265411882950759345056149650194623020034160613335899667019478714122893893602793129571300818603011371328012639645333225310299210587007996264758996487153829487645413735989861246419837010099185751453204125224782310583


print(f"random key: {randomkey}")

A = alice.computePublicKey(randomkey)

B = 26191418673309862885497838712018782099965391239161319520707078612856510774887625915044654950148663347249204376615201994320978085686859356910968244641333481421866572074292991604076045789111845085315168079676987267489983459090496016822364848511468307097480380221031328930783860205720789346677686626012536529311

print(f'A: {A}')

ky = alice.computePrivateKey(B, randomkey)

print(f'Compute value {ky}')



