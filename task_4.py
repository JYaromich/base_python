def my_func(x: float, y: int) -> float:
    """Функция возводит действительное число в отрицательную степень

    :param x: число которое нужно возвести в степень
    :param y: степень числа (со знаком минус)
    :return: число x, возведенное в степень y
    """
    if y > 0:
        print('Ошибка введите отрицательную степень числа!')
        return None
    power = abs(y)
    denominator = x
#    return x ** -2 #Решение для способа №1
    for i in range(1, power):
        denominator *= denominator
    return 1 / denominator



try:
    number = float(input('Введите число которое нужно возвести в степень: '))
    input_power = int(input('Введите отрицательную степень: '))
    result = my_func(number, input_power)
    if result:
        print(f'Результат возведениея числа {number} в степень {input_power}: {result}')
except ValueError:
    print('Введите корректное действительное число')
