import math
a = float(input())
b = float(input())
c = float(input())
D = ((b ** 2) - (4 * a * c)) ** (1 / 2)
x1 = (- b - D) / (2 * a) 
x2 = (- b + D) / (2 * a)
if x1 == x2:
    if x1 - int(x1) <= 0.1 and x2 - int(x2) <= 0.1:
        print(int(x1))
    else:
        print(x1)
if x1 != x2:
    if x1 - int(x1) <= 0.1 and x2 - int(x2) <= 0.1:
        print(int(x1), int(x2))
    else:
        print(x1, x2)
    
        

    
