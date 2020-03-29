a = int(input())
d = int(input())
c = int(input())
p = (a + d + c) / 2
S = ((p - a) * (p - d) * (p - c) * p)  ** (1 / 2)
if S == int(S):
    print(int(S))
elif S > int(S):
    print(round(S,6))
