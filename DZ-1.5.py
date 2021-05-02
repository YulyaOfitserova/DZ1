proceeds = int(input('Введите значение выручки в рублях: '))
outlay = int(input('Введите значение издержек в рублях: '))

if proceeds > outlay:
    print('У вас прибыльный бизнес!')

    profit = proceeds - outlay
    rent = (profit / proceeds) * 100
    print(f'Рентабельность выручки -  {rent}%')

    number = int(input('Введите количество сотрудников: '))
    prof_num = profit / number
    print(f'Прибыль на одного сотрудника - {round(prof_num, 2)} рублей.')

elif proceeds == outlay:
    print('У вас нет прибыли в этом году, но вы окупили расходы.')

else:
    print('Ваш бизнес терпит убытки.')

