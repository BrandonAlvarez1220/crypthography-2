from EllipticCurve import EllipticCurve

def buildCurve(a,b,p):
    result = curve.elipticCurve(a,b,p)
    qr,sr = curve.quadraticResidues(p)

    return result,qr,sr


#Instance of EllipticCurve class
curve = EllipticCurve()

#Generate a random parameters of an elliptic curve
a, b, p = 1, 1, 5

#Generate the results of the function
result, qr, sr = buildCurve(a,b,p)

#Get points of elliptic curve
points = curve.getPoints(qr, result)

#Get negative points
npoints = curve.negativePoints(qr,result,p)


print(f"Curva: x^3 +{a}x + {b} en Z{p}\n")
print(f'Puntos de la curva:\n{points}')
print(f'\n-P:\n{npoints}')

curve.sumPoints(a,b,p,x1=0,y1=19,x2=39,y2=4)





