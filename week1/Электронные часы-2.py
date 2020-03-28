num = int(input())
h = (num // 3600) % 24
m1 = num // 60 % 60 // 10
m2 = num // 60 % 60 % 10
s1 = num % 60 // 10
s2 = num % 10
print(h,":",m1,m2,":",s1,s2,sep="")

