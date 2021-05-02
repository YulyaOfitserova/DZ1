a = 4
b = 8
i = 1

print("1-й день:", a)

while a < b:
    a *= 1.1
    i += 1
    result = (f'{i}-й день:' 
              f'{round(a, 2)}')
    print(result)

answer = (f'Ответ: На {i}-й день спортсмен достиг результата - не менее '
          f'{b} км.')
print(answer)