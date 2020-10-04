def dev(dev_1: float, dev_2: float) -> float:
    """Функция делит число a на число b

    a - делимое
    b - делитель

    """
    try:
        return dev_1 / dev_2
    except ZeroDivisionError:
        print("Ошибка! Деление на 0 невозможно")


while True:
    try:
        a = float(input('Введите делимое: '))
        b = float(input('Введите делитель: '))
        result = dev(a, b)
        if result:
            print(f'Результат деления: {round(result, 3)}')
            break
        else:
            print()
    except ValueError:
        print('Ошибка! Введите действительные числа\n')
