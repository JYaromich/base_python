def my_func(f_1: float, f_2: float, f_3: float) -> float:
    """ Функция возвращает сумму 2-х наибольших чисел

    :param f_1: число №1
    :param f_2: число №2
    :param f_3: чссло №3
    :return: сумму наибольших
    """

    return sum((f_1, f_2, f_3)) - min(f_1, f_2, f_3)


try:
    input_f1 = float(input('Введите число №1: '))
    input_f2 = float(input('Введите число №2: '))
    input_f3 = float(input('Введите число №3: '))

    print(f"Сумма двух наибольших значений: {my_func(input_f1, input_f2, input_f3)}")
except ValueError:
    print('Ошибка! Введите корректно числа')
