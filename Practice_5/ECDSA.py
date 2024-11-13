import math
import random


class ECDSA:

    def __init__(self, p, a, b, G, q):
        self.p = p
        self.a = a
        self.b = b
        self.G = G
        self.q = q

    def isPoint(self):

        x, y = self.G

        y2 = (math.pow(x, 3) + self.a * x + self.b) % self.p
        sr = (math.pow(y, 2)) % self.p

        if (y2 == sr):
            return True
        else:
            return False

    def find_mod_inv(self, a, m):

        for x in range(1, m):
            if (a % m) * (x % m) % m == 1:
                return x
        raise Exception("The modular inverse does not exist.")

    def euclides_extendido(self, a, b):
        x0, x1, y0, y1 = 1, 0, 0, 1
        while b != 0:
            q, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return x0 % self.p

    def sum_points(self, P, Q):
        x1, y1, z1 = P
        x2, y2, z2 = Q

        if z1 == 0:
            return Q
        if z2 == 0:
            return P

        if P == Q:
            s = (3 * x1 ** 2 + self.a * z1 ** 2) * self.euclides_extendido(2 * y1 * z1, self.p) % self.p
        else:
            # Fórmula para suma de puntos
            s = (y2 * z1 - y1 * z2) * self.euclides_extendido(x2 * z1 - x1 * z2, self.p) % self.p

        x3 = (s ** 2 - x1 * z2 - x2 * z1) % self.p
        y3 = (s * (x1 * z2 - x3) - y1 * z2) % self.p
        z3 = (z1 * z2) % self.p

        return x3, y3, z3

    def scalar_multiplication(self, k, P):

        result = (0, 1, 0)  # Punto al infinito
        addend = P

        while k > 0:
            if k % 2 == 1:
                result = self.sum_points(result, addend)
            addend = self.sum_points(addend, addend)
            k //= 2

        return result

    def generateKeys(self):

        # Generate private key
        #d = random.randint(1, self.q)

        d = int(input("Digita el valor de d: "))

        # Deconstructing A
        A = self.G

        # Deconstructing B
        B = self.scalar_multiplication(d, self.G)

        # Generate public key
        kpub = (self.p, self.a, self.b, self.q, A, B)

        # Save public key in a text file
        file = open("PublicKey.txt", "w")
        file.write(str(kpub))
        file.write('\n' + str(d))

        return kpub, d

    def signatureGeneration(self, m):

        ke = random.randint(1, self.q - 1)
        R = self.scalar_multiplication(ke, self.G)
        r = R[0]
        d = self.generateKeys()[1]
        s = ((m + (d * r)) * self.find_mod_inv(ke, self.q)) % self.q

        return int(r), int(s)

    def signatureVerification(self, filename, sign, m):

        try:
            file = open(filename)
            content = eval(file.readline())

            r, s = sign

            w = self.find_mod_inv(s, self.q)
            u1 = int((w * m) % self.q)
            u2 = int((w * r) % self.q)

            if u1 < 0:
                u1 = self.q + (u1 % self.q)

            if u2 < 0:
                u2 = self.q + (u2 % self.q)

            x1 = int(input("Digita el valor de x: "))
            y1 = int(input("digita el valor de y: "))
            point = (x1, y1, 1)

            ua = self.scalar_multiplication(u1, content[4])

            ub = self.scalar_multiplication(u2, point)

            P = self.sum_points(ua, ub)

            file.close()

            # Comprobar si las cordenadas son iguales

            if P[0] == r:
                return True
            else:
                return False

        except Exception as e:
            print(f"Error to read file: {e}")


def menu():
    # Generation of parameteres:
    # p, a, b, G, q
    test = ECDSA(191, 1, 6, (0, 31, 1), 197)
    #test = ECDSA(53, 2, 10, (3, 19, 1), 59)
    print(f'Public key: {test.generateKeys()[0]}')

    while True:
        print("1-Realizar firma")
        print("2-Verificar firma")
        print("3-Salir")
        op = int(input("Digita una opcion: "))

        match op:
            case 1:
                m = int(input("Digita el valor de m:"))
                P = test.signatureGeneration(m)
                print(f'Las coordenadas (r,s) son: {P}')

            case 2:
                r = int(input("Digita el valor de r: "))
                s = int(input("Digita el valor de s: "))
                sign = (r, s)
                m = int(input("Digita el valor de m: "))

                ver = test.signatureVerification("PublicKey.txt", sign, m)
                print(f'La verificación de la firma es: {ver}')

            case 3:
                break


menu()
