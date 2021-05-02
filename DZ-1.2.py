time = int(input('Здравствуйте! Введите время в секундах: '))

hour = time // 3600
minute = (time % 3600) // 60
sec = time % 60

result = (f'{hour}:'
          f'{minute}:'
          f'{sec}')

print(result)






        






