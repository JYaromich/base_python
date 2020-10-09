from functools import reduce
print(f'Результат вычисления: \n'
      f'{reduce((lambda p_1, p_2: p_1 * p_2), [el for el in range(100, 1001) if el % 2 == 0])}')
