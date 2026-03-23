# BinaryTest/test03.py

a = 0b1100
b = 0b1010

print(bin(a|b))

print(bin(a^b))

print(bin(~a))
print(bin(~a & 0xF))