p = int(input())
x = int(input())
y = int(input())
m1 = 100 * x + y
m2 = int(m1 * (100 + p) / 100)
print(m2 // 100, m2 % 100)
