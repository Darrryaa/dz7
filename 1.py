count = 0
a = []
for i in range(100, 999+1):
    if i%17==0:
        count+=i
        a.append(i)
print(a, count, sep = '\n')
