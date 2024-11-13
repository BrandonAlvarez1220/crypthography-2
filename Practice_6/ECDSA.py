from random import randint
from Crypto.PublicKey import ECC
from base64 import b64encode
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
from base64 import b64decode



# Function to generate key pair
def generate_key_pair():

    # Generate private key
    private_key = ECC.generate(curve='P-256') # P-192, P-224

    # Save public key
    public_key = private_key.public_key()

    with open("private_key.txt", "w") as priv_file:
        priv_file.write(b64encode(private_key.export_key(format='DER')).decode('utf-8'))

    with open("public_key.txt", "w") as pub_file:
        pub_file.write(b64encode(public_key.export_key(format='DER')).decode('utf-8'))

def get_curve_order():
    return int("FFFFFFFF00000000FFFFFFFFFFFFFFFFBCE6FAADA7179E84F3B9CAC2FC632551", 16)


# Function to generate signature
def sign_message(m):

    with open("private_key.txt", "r") as priv_file:
        private_key = ECC.import_key(b64decode(priv_file.read()))

    q = get_curve_order()

    if not (0 < m < q):
        raise ValueError("El mensaje debe ser un entero entre 0 y q")

    # Create hash(x)
    h = SHA256.new(str(m).encode('utf-8'))

    # Create signature
    signer = DSS.new(private_key, 'fips-186-3')

    # Get pair r and s
    signature = signer.sign(h)

    # deconstructing r, s
    r, s = int.from_bytes(signature[:len(signature) // 2], 'big'), int.from_bytes(signature[len(signature) // 2:],
                                                                                  'big')
    return r, s


# Verify a signature
def verify_signature(m, r, s):

    with open("public_key.txt", "r") as pub_file:
        public_key = ECC.import_key(b64decode(pub_file.read()))

    q = get_curve_order()

    if not (0 < m < q):
        raise ValueError("El mensaje debe ser un entero entre 0 y q")

    # Create hash(x)
    h = SHA256.new(str(m).encode('utf-8'))

    # Constructing signature
    signature = r.to_bytes(32, 'big') + s.to_bytes(32, 'big')

    # Verify signature
    verifier = DSS.new(public_key, 'fips-186-3')
    try:
        verifier.verify(h, signature)
        return True
    except ValueError:
        return False



def test_program():

    generate_key_pair()

    for i in range(5):
        # Generate m
        q = get_curve_order()
        m = randint(1, q - 1)

        # Signature generation
        r, s = sign_message(m)
        print(f"Firma para el mensaje: {m}:")
        print(f"r: {r}")
        print(f"s: {s}")

        # Verify the signature
        is_valid = verify_signature(m, r, s)
        print(f"¿Firma válida?: {is_valid}")
        print("-" * 40)

'''
# Ejemplo de uso
q = get_curve_order()

# Mensaje y firma generados previamente
m = randint(1, q - 1)  # Mensaje aleatorio para probar
r, s = sign_message(m)  # Firma del mensaje m

# Verificación de la firma
is_valid = verify_signature(m, r, s)
print("¿Firma válida?:", is_valid)
'''



'''
TEST
generate_key_pair()

q = get_curve_order()

# Generar un mensaje aleatorio en el rango 0 < m < q
m = randint(1, q - 1)
r, s = sign_message(m)
print("r:", r)
print("s:", s)

'''
