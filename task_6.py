from itertools import count, cycle

try:
    border_count = int(input('Введите границу до которой нужно выполнять генерацию '))
    start = int(input('Введите значение, c которого нужно начать генерировать целые числа '))
    if border_count > start:
        for el in count():
            if el > border_count:
                break
            print(el)
        counter = 0
        print('-' * 100)
        for el in cycle(['You', 'are', 'cool']):
            print(el)
            if counter > border_count:
                break
            counter += 1
    else:
        print('Ошибка! Граница не может быть меньше числа с которого '
              'должен начаться отсчет')
except ValueError:
    print('Ошибка! '
          'Для генерации целых чисел, граница генерации тоже должна быть целым числом')
