import random
nyx=[random.randint(0,10) for i in range(10)]
print(nyx)
z=int(input("Укажите число:"))
x=nyx.index(z)
print("Число "+str(z)+"  находится в списке под номером  "+str(x))