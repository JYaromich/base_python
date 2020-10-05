def sum_number(number: str) -> float:
    """Функция подсчитывает сумму числе в строке разделенных пробелами

    :param number: строка с числами разделенными пробелами
    :return: сумма чисел в строке
    """
    list_number = number.split()
    result = 0
    try:
        for number in list_number:
            result += float(number)
    except ValueError:
        print('Ошибка при вводе данных. Необходимо вводить только цифры через пробелы, '
              'если вы хотите выйти из программы введите - q')
    finally:
        return result


print("Программа сумматор чисел.\nДля выхода из программы напишите 'q'\n")
total_count = 0
while True:
    str_number = input('Введите строку числе разделенную пробелом: ')
    if str_number.count('q'):
        total_count += sum_number(str_number[:str_number.index('q')])
        print(f'Общий счет - {total_count}')
        break
    else:
        temp_count = sum_number(str_number)
        total_count += temp_count
        print(f'Сумма в строку - {temp_count}\nОбщий счет - {total_count}\n')
