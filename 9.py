n = int(input())
k = int(input())
r = int(input())
t=1
while n < r:
    n = n+n*(k/100)
    t+=1
print(t)

