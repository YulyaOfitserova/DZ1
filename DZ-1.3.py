num = input('Введите любое целое число: ')
dlina = int(len(num))
number = int(num)

num_1 = number * (10 ** dlina) + number
num_2 = num_1 * (10 ** dlina) + number
sum = number + num_1 + num_2

print(number, '+', num_1, '+', num_2, "=", sum)