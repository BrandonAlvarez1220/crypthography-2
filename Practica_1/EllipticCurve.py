import random
from sympy import *

class EllipticCurve:

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

    # Function to generate the parameters of an elliptic curve
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


    def getPoints(self,qr,evaluate):

        points = list()

        for i, value in enumerate(evaluate):
            for j,qrValue in enumerate(qr):

                if value == qrValue:
                    points.append([i,j])

        return points
