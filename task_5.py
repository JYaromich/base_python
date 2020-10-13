from random import randint

try:
    with open('task_5.txt', 'w') as task_file:
        for i in range(randint(1, 5)):
            print(randint(1, 100), end=' ', file=task_file)
    with open('task_5.txt', 'r') as input_file:
        line = input_file.read()
        print(sum(map(int, line.split())))
except IOError:
    print('Ошибка при работе с файлом')
except ValueError:
    print('Ошибка при вычислении суммы')
