from Crypto.Util import number
from DiscreteLogarithm import DiscreteLogarithm

'''
prime = number.getPrime(1024)
print(prime)
'''

dlp = DiscreteLogarithm()

x1 = dlp.discrete_log(10007, 5, 9012)
x2 = dlp.discrete_log(100003, 2, 100002)
x3 = dlp.discrete_log(100000000003, 2, 1922556950)
x4 = dlp.discrete_log(500000009, 3, 406870124)
x5 = dlp.discrete_log(500000009, 3, 187776257)

print("Results \n")
print(f'x = {x1}')
print(f'x = {x2}')
print(f'x = {x3}')
print(f'x = {x4}')
print(f'x = {x5}')

print("\n Curvas elipticas ")

# Parámetros de las curvas elípticas para los casos dados
params = [
    {"p": 113, "a": 1, "b": 9, "G": (47, 22), "P": (52, 53)},
    {"p": 503, "a": 11, "b": 1, "G": (457, 404), "P": (459, 58)},
    {"p": 5009, "a": 1, "b": 1, "G": (359, 1928), "P": (1942, 2938)},
    {"p": 1000003, "a": 1000, "b": 1, "G": (917459, 678095), "P": (798677, 191330)},
    {"p": 500000009, "a": 1, "b": 99, "G": (377863415, 222914743), "P": (477613302, 314579681)}
]

dl = DiscreteLogarithm()

# Resolviendo para cada conjunto de parámetros
for param in params:
    p = param["p"]
    a = param["a"]
    b = param["b"]
    G = param["G"]
    P = param["P"]
    x = dl.discrete_logCurve(a, b, p, G[0], G[1], P[0], P[1])
    print(f"Para p={p}, a={a}, b={b}, G={G}, P={P}, x es: {x}")
