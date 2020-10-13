try:
    with open('new_file.txt', 'w') as new_file:
        while True:
            input_str = input('Введите строку для сохранения в '
                              'файл new_file.txt (для выхода ничего не вводя, нажмите интер): ')
            if not input_str:
                break
            print(input_str, file=new_file)
except IOError:
    print('Произошла ошибка при записи в файл new_file.txt')
