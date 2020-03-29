a = float(input())
if round((a % 1),9) < 0.5:
    print(int(a))
elif round((a % 1),9) >= 0.5:
    print(int(a) + 1)
