def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = 66528
b = 52920
print("FLAG =", gcd(a, b))