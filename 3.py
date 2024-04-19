import math
n = int(input())
if math.sqrt(n)%1 == 0:
    print('является квадратом')
else:
    print('не является')