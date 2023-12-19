def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    gcd, u, v = extended_gcd(b, a % b)
    return gcd, v, u - (a // b) * v

p = 26513
q = 32321

print("FLAG =", min(extended_gcd(p, q)))