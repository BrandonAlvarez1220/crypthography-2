import math
class DiscreteLogarithmEllipticCurve:

    def __init__(self, p, a, b, G, P):
        self.p = p
        self.a = a
        self.b = b
        self.G = G  # G(x, y, z)
        self.P = P  # P(x, y, z)

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

    def baby_step_giant_step(self):
        """ P = x * G """
        m = math.isqrt(self.p) + 1

        baby_steps = {}
        current_point = self.G
        for j in range(m):
            baby_steps[current_point] = j
            current_point = self.sum_points(current_point, self.G)

        # Calcular inverso mG
        mG = self.scalar_multiplication(m, self.G)
        mG_neg = (mG[0], (-mG[1]) % self.p, mG[2])

        # Buscar el valor de x
        current_point = self.P
        for i in range(m):
            if current_point in baby_steps:
                return i * m + baby_steps[current_point]
            current_point = self.sum_points(current_point, mG_neg)

        return None


# Parameters of the problems
instances_curve = [
    {"p": 113, "a": 1, "b": 9, "G": (47, 22, 1), "P": (52, 53, 1)},
    {"p": 503, "a": 11, "b": 1, "G": (457, 404, 1), "P": (459, 58, 1)},
    {"p": 5009, "a": 1, "b": 1, "G": (359, 1928, 1), "P": (1942, 2938, 1)},
    {"p": 1000003, "a": 1000, "b": 1, "G": (917459, 678095, 1), "P": (798677, 191330, 1)},
    {"p": 500000009, "a": 1, "b": 99, "G": (377863415, 222914743, 1), "P": (477613302, 314579681, 1)}
]

for instance in instances_curve:
    solver = DiscreteLogarithmEllipticCurve(instance['p'], instance['a'], instance['b'], instance['G'], instance['P'])
    x = solver.baby_step_giant_step()
    print(
        f"Para p={instance['p']}, a={instance['a']}, b={instance['b']}, G={instance['G']}, P={instance['P']}, x es: {x}")
