import random
import hashlib

#curve configuration
# y^2 = x^3 + a*x + b = y^2 = x^3 + 7
a = 0; b = 7
 
#base point
x0 = 55066263022277343669578718895168534326250603453777594175500187360389116729240
y0 = 32670510020758816978083085130507043184471273380659243275938904335757337482424
 
#finite field
mod = pow(2, 256) - pow(2, 32) - pow(2, 9) - pow(2, 8) - pow(2, 7) - pow(2, 6) - pow(2, 4) - pow(2, 0)
order = 115792089237316195423570985008687907852837564279074904382605163141518161494337


def add_points(P, Q, p):
    x1, y1 = P
    x2, y2 = Q
     
    if x1 == x2 and y1 == y2:
        beta = (3*x1*x2 + a) * pow(2*y1, -1, p)
    else:
        beta = (y2 - y1) * pow(x2 - x1, -1, p)
     
    x3 = (beta*beta - x1 - x2) % p
    y3 = (beta * (x1 - x3) - y1) % p
     
    is_on_curve((x3, y3), p)
         
    return x3, y3
 
def is_on_curve(P, p):
    x, y = P
    assert (y*y) % p == ( pow(x, 3, p) + a*x + b ) % p

def apply_double_and_add_method(G, k, p):
    target_point = G
     
    k_binary = bin(k)[2:] #0b1111111001
     
    for i in range(1, len(k_binary)):
        current_bit = k_binary[i: i+1]
         
        # doubling - always
        target_point = add_points(target_point, target_point, p)
         
        if current_bit == "1":
            target_point = add_points(target_point, G, p)
     
    is_on_curve(target_point, p)
     
    return target_point


def main():
    # Generate private key
    privateKey = 75263518707598184987916378021939673586055614731957507592904438851787542395619
    G = (x0, y0)  # Base point

    # Calculate public key
    publicKeyX, publicKeyY = apply_double_and_add_method(G, privateKey, mod)
    print("Public key: (", publicKeyX, ", ", publicKeyY, ")")

    # Generate random key and random point
    randomKey = random.getrandbits(128) # GPT'ye sordum. Neden 128 diye. Bunu da ekle
    randomPointX, randomPointY = apply_double_and_add_method(G, randomKey, mod)
    print("Random point: (", randomPointX, ", ", randomPointY, ")")

    # Hash the message
    message = b"ECC beats RSA"
    hashHex = hashlib.sha1(message).hexdigest()
    hashValue = int(hashHex, 16)

    print("Message: ", message)
    print("Hash: ", hashValue)

    # Signature generation
    r = randomPointX % order
    s = (hashValue + (r * privateKey)) * pow(randomKey, -1, order)
    s %= order

    print("Signature")
    print("r: ", r)
    print("s: ", s)

    # Signature verification
    w = pow(s, -1, order)
    u1 = apply_double_and_add_method(G, (hashValue * w) % order, mod)
    u2 = apply_double_and_add_method((publicKeyX, publicKeyY), (r * w) % order, mod)
    checkpoint = add_points(u1, u2, mod)

    if checkpoint[0] == r:
        print("Signature is valid...")
    else:
        print("Invalid signature detected!!!")

main()
