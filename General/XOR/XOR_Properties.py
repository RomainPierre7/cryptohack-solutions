import pwn

KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313")
KEY2_XOR_KEY1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e")
KEY2_XOR_KEY3 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1")
FLAG_XOR_3 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")

KEY2 = pwn.xor(KEY2_XOR_KEY1, KEY1)
KEY3 = pwn.xor(KEY2_XOR_KEY3, KEY2)

FLAG_XOR_2 = pwn.xor(FLAG_XOR_3, KEY3)
FLAG_XOR_1 = pwn.xor(FLAG_XOR_2, KEY2)
FLAG = pwn.xor(FLAG_XOR_1, KEY1)

print("FLAG =", FLAG.decode('utf-8'))