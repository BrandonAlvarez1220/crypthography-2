import math
import random
from sympy import *

class EllipticCurve:

    def getPoints(self,qr,evaluate):

        points = list()
        points.append(["inf", "inf"])

        for i, value in enumerate(evaluate):
            for j,qrValue in enumerate(qr):

                if value == qrValue:
                    points.append([i,j])

        return points

    # Function to get quadratic residues & SR
    def quadraticResidues(self, p):

        qr = list()
        sr = {}

        for i in range(0, p):
            res = pow(base=i, exp=2) % p
            qr.append(res)

            if res not in sr:
                sr[res] = [i]
            else:
                sr[res].append(i)

        return qr, sr

    # Function to evaluate an Elliptic Curve
    def elipticCurve(self, a, b, p):

        result = list()

        for i in range(0, p):
            y = (pow(i, 3) + (a * i) + b) % p
            result.append(y)

        return result
    def generateParameters(self):

        p = randprime(11, 1000)
        a = random.randint(1, p - 1)
        b = random.randint(1, p - 1)
        function = 0

        # Evaluate discriminant
        while function != 0:
            function = (4 * (a ** 3)) + (27 * (b ** 2))

            if function == 0:
                a = random.randint(1, p - 1)
                b = random.randint(1, p - 1)


        return a, b, p


    def isPoint(self,a,b,p,x,y):

        y2= (math.pow(x,3)+a*x+b)%p
        sr = (math.pow(y,2)) % p

        if(y2 == sr):
            return True
        else:
            return False

    def negativePoints(self,qr,evaluate,p):

        points = list()
        points.append(["inf","inf"])

        for i, value in enumerate(evaluate):
            for j,qrValue in enumerate(qr):

                if value == qrValue:
                    y = (j*-1) % p
                    points.append([i, y])

        return points

    def euclides_extendido(self,alpha, n):
        a, b = alpha, n
        x, y = 1, 0
        # Actualización hasta que b es 0
        while b != 0:
            q, r = divmod(a, b)
            a, b = b, r
            x, y = y, x - q * y
            # Si x es negativo después del algoritmo, se agrega n a x para asegurarse de que el resultado esté en el rango [0, n).
        if x < 0:
            x += n
        return x

    def doublingPoint(self,a,b,p,x1,y1):

        if x1 == 'inf' or y1 == 'inf':
            print('Es el punto al infinito:  (inf,inf)')

        if self.isPoint(a,b,p,x1,y1):

            #Calculate s when P = Q
            s = ((3 * math.pow(x1, 2) + a) * self.euclides_extendido(2 * y1, p)) % p
            if (s == 0):
                print("El punto resultante es el infinito")
            else:
                x3 = (math.pow(s, 2) - x1 - x1) % p
                y3 = (s * (x1 - x3) - y1) % p
                print(f"\nEl doblado del punto ({x1}, {y1}) es: ({int(x3)},{int(y3)})")

        else:
            print('El punto no pertenece a la curva')


    def sumPoints(self,a,b,p,x1,y1,x2,y2):

        if self.isPoint(a, b, p, x1, y1) and self.isPoint(a, b, p, x2, y2):

            #Special cases
            if x1 == 'inf' or y1 == 'inf':
                print(f'El resultado es de la suma es:  ({x2},{y2})')

            if x2 == 'inf' or y2 == 'inf':
                print(f'El resultado es de la suma es:  ({x1},{y1})')

            if x1 == x2 and y1 == y2:
                self.doublingPoint(a,b,p,x1,y1)
            else:
                #Calculate s for P != Q
                s = ((y2 - y1) * (self.euclides_extendido(x2 - x1, p))) % p
                if s == 0:
                    print('El punto es el infinito')
                else:
                    x3 = (math.pow(s, 2) - x1 - x2) % p
                    y3 = (s * (x1 - x3) - y1) % p
                    print(f'\nLa suma de los puntos ({x1},{y1}) y ({x2},{y2}) es : ({int(x3)},{int(y3)})')
        else:
            print('Punto invalido')

