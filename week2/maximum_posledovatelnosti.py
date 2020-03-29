a = int(input())
maxA = a
while a != 0:
    a = int(input())
    if a == 0:
        break
    if a > maxA:
        maxA = a
print(maxA)
