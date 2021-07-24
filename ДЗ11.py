import random
list=[random.randint(0,10) for i in range(10)]
print(list)
a = int(input("Какое число заменить?: "))
b = int(input("На какое число заменить?: "))
for c in range(len(list)):
    if list[c] == a:
        list[c] = b

print (list)