num = int(input('Введите любое целое положительное число: '))
b = 0

while num > 0:
    a = num % 10
    num //= 10
    if a >= b:
        b = a

print(b)
