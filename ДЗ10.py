n = int(input("введите число: "))

b = 0

while n > 0:
    a = n % 10
    b = b + a
    n = n // 10

print("Сумма:", b)