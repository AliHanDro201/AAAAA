n0 = 0
n = int(input())
for i in range(n):
    a = int(input())
    if a == 0:
        n0 +=1
if n0 == 0:
    print('No')
else:
    print('Yes')
