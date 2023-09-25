import pwn
import re

data = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d")

for i in range(2 ** 8):
    flag = pwn.xor(data, i)
    if re.search("crypto", str(flag)):
        print("FLAG =", flag)