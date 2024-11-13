from EllipticCurve import EllipticCurve

def buildCurve(a,b,p):
    result = curve.elipticCurve(a,b,p)
    qr,sr = curve.quadraticResidues(p)

    return result,qr,sr


#Instance of EllipticCurve class
curve = EllipticCurve()

#Generate a random parameters of an elliptic curve
a,b,p = 1,10,11

#Generate the results of the function
result,qr,sr = buildCurve(a,b,p)

#Get points of elliptic curve
x = curve.getPoints(qr,result)


print(f"a parameter: {a}, b parameter {b}, p number {p} \n")
print(f"Results of Evualte a function x3 + ax +b mod p \n {result} \n")
print(f"Quadratic Residues \n {qr} \n")
print(f"Square roots \n {sr} \n")
print(f"Points of Elliptic Curve:  \n * , {x} \n")
print(f"Total number of points: {len(x)+1} ")


file = open("ParametersofCurve.txt","w")
file.write(f"a parameter: {a}, b parameter {b}, p number {p} \n\n")
file.write('List of points \n'+"*, "+str(x))
file.write(f"\n\nTotal number of points: {len(x)+1}")



