def fact(n: int) -> 'generator object':
    """
    Функция возвращает генератор на последовательно факториалов от 1 до n
    :param n: конеченое значение последовательности факториалов
    :return: генератор на поседовательность факториалов
    """
    if n > 0:
        for f_1 in range(1, n + 1):
            result = 1
            for r in range(1, f_1 + 1):
                result *= r
            yield result
    elif n == 0:
        yield 1
    else:
        print('Ошибка. Введите действительное положительное число')
        yield -1


try:
    for el in fact(int(input('Введите значение конца последовательно n = '))):
        print(el)
except ValueError:
    print("Ошибка! Необходимо вводить только числа")
