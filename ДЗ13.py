import random
a=[random.randint(0,10) for i in range(10)]
b=[random.randint(0,10) for i in range(10)]
c=[]
print(a)
print(b)
for i in a:
    if i in c:
        continue
    for j in b:
        if i == j:
            c.append(i)
            break
print(c)