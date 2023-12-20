p = 29
ints = [14, 6, 11]

res = []
for a in range(1, p):
    if (a ** 2) % p in ints:
        res.append(a)

print("FLAG =", min(res))