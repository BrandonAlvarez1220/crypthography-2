import math


class DiscreteLogarithmZp:

    def __init__(self, p, g, beta):
        self.p = p
        self.g = g
        self.beta = beta

    def euclides_extendido(self, a, b):
        x0, x1, y0, y1 = 1, 0, 0, 1
        while b != 0:
            q, a, b = a // b, b, a % b
            x0, x1 = x1, x0 - q * x1
            y0, y1 = y1, y0 - q * y1
        return x0

    def baby_step_giant_step(self):
        n = math.isqrt(self.p) + 1

        # Baby step: g^j mod p para j en [0, n-1]
        baby_steps = {}
        for j in range(n):
            baby_steps[pow(self.g, j, self.p)] = j

        # Calcular  inverso  de g mod p
        g_inv_n = pow(self.g, -n, self.p)

        # Giant step: buscar el valor de x
        for i in range(n):
            g_step_value = (self.beta * pow(g_inv_n, i, self.p)) % self.p
            if g_step_value in baby_steps:
                return i * n + baby_steps[g_step_value]

        return None


# Problems
instances = [
    {"p": 10007, "g": 5, "beta": 9012},
    {"p": 100003, "g": 2, "beta": 100002},
    {"p": 100000000003, "g": 2, "beta": 1922556950},
    {"p": 500000009, "g": 3, "beta": 406870124},
    {"p": 500000009, "g": 3, "beta": 187776257}
]


print("Resultados del ejercicio 1 \n")

for instance in instances:
    solver = DiscreteLogarithmZp(instance['p'], instance['g'], instance['beta'])
    x = solver.baby_step_giant_step()
    print(f"Para p={instance['p']}, g={instance['g']}, beta={instance['beta']}, x es: {x}")
