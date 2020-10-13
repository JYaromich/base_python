try:
    with open('task_2.txt', 'r') as input_file:
        count_line = 0
        for line in input_file:
            count_line += 1
            print(f'Текст строки: {line}', end='')
            print(f'Строка # {count_line}, количество слов - {len(line.split())}')
except IOError:
    print('Возникла ошибка при работе с файлами')
