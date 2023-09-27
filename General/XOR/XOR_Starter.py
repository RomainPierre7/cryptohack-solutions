string = "label"
integer = 13

string_unicode = [ord(i) for i in string]
xor_unicode = [i ^ integer for i in string_unicode]
xor_string = "".join([chr(i) for i in xor_unicode])

print("FLAG =", xor_string)