a = int(input())
b = int(input())
c = a // b
e = ((c + 2) // (c + 1)) % 2
d = (c + 1) % 2
res = a * e + b * d
print(res)
