# 3 * d = 1 [13]
# 3 ** 12 = 1 [13] (Fermat's little theoreme)
# d = 3 ** 11 [13]

element = 3
modulo = 13

print("FLAG =", (3 ** (modulo - 2)) % 13)