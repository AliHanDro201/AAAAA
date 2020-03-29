a = int(input())
b = int(input())
if a < b:
    print(*list(range(a, b + 1)))
else:
    print(*list(range(a, b - 1, -1)))
