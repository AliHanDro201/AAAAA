Cyfry = [int(s) for s in input().split()]
BilIliNet = set()
for num in Cyfry:
    if num in BilIliNet:
        print('YES')
    else:
        print('NO')
        BilIliNet.add(num)
