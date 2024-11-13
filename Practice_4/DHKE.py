import math

class DiffieHellmanEllipticCurve:
    def __init__(self, p, a, b, G):
        self.p = p
        self.a = a
        self.b = b
        self.G = G

    # Algoritmo de Euclides extendido
    def euclides_extendido(self, a, b):
        x0, x1, y0, y1 = 1, 0, 0, 1
        while b != 0:
            q, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return x0 % self.p

    # Suma de puntos en la curva elíptica
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
            s = (y2 * z1 - y1 * z2) * self.euclides_extendido(x2 * z1 - x1 * z2, self.p) % self.p


        x3 = (s ** 2 - x1 * z2 - x2 * z1) % self.p
        y3 = (s * (x1 * z2 - x3) - y1 * z2) % self.p
        z3 = (z1 * z2) % self.p

        return (x3, y3, z3)

    def scalar_multiplication(self, k, P):
        result = (0, 1, 0)  # Punto al infinito
        addend = P

        while k > 0:
            if k % 2 == 1:
                result = self.sum_points(result, addend)
            addend = self.sum_points(addend, addend)
            k //= 2

        return result


def main():

    ''''
    p = 127
    a = 10
    b = 1
    G = (0, 1, 1)
    '''

    p = 191
    a = 1
    b = 6
    G = (0, 31, 1)

    dh = DiffieHellmanEllipticCurve(p, a, b, G)

    k_A = int(input("Introduce la clave privada k_A (2 ≤ k_A ≤ p-1): "))

    A = dh.scalar_multiplication(k_A, G)
    print(f"Punto público A = k_A * G: ({A[0]}, {A[1]}, {A[2]})")

    xb = int(input("Introduce el valor de x de BOB: "))
    xy = int(input("Introduce el valor de y de BOB: "))

    point_bob = (xb, xy, 1)

    bob = dh.scalar_multiplication(k_A, point_bob)
    print(f"Punto resultante B = k_A * BOB: ({bob[0]}, {bob[1]}, {bob[2]})")



    #B = dh.scalar_multiplication()


if __name__ == "__main__":
    main()
