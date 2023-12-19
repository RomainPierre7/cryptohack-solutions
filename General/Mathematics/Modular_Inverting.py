# (3 * d) % 13 = 1
# (3 ** 12) % 13 = 1 (Fermat's little theoreme)
# d = (3 ** 11) % 13

element = 3
modulo = 13

print("FLAG =", (3 ** (modulo - 2)) % 13)