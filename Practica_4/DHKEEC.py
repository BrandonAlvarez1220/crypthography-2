import random

from Crypto.Util import number
class DHKEEC:

    def __init__(self, a, b, p, g):

        self.a = a
        self.b = b
        self.p = p
        self.g = g
        self.qr, self.sr = self.quadraticResidues()
        self.curve = self.elipticCurve()

    def elipticCurve(self):

        result = list()

        for i in range(0, self.p):
            y = (pow(i, 3) + (self.a * i) + self.b) % self.p
            result.append(y)

        return result

    def getPoints(self, qr, evaluate, z=1):

        points = list()
        points.append([0,1,0])

        for i, value in enumerate(evaluate):
            for j,qrValue in enumerate(qr):

                if value == qrValue:
                    points.append([i, j, z])

        return points

    # Function to get quadratic residues & SR
    def quadraticResidues(self):

        qr = list()
        sr = {}

        for i in range(0, self.p):
            res = pow(base=i, exp=2) % self.p
            qr.append(res)

            if res not in sr:
                sr[res] = [i]
            else:
                sr[res].append(i)

        return qr, sr

    def randomkey(self):
        return random.randint(2, len(self.getPoints(self.qr, self.curve)))


dh = DHKEEC(a=1, b=1, p=5, g=(5, 6))
curve = dh.elipticCurve()
qr = dh.quadraticResidues()[0]

print(f'Points: {dh.getPoints(qr,curve)}')

