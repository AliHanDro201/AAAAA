a = list(map(int,input().split()))
index = 0
e = a[0]
for ind, val in enumerate(a):
    if val > e or val == e:
        index, e = ind, val
        
print( e, index )
