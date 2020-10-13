try:
    min_salary_personal = {}
    average_salary = 0
    person_count = 0
    with open('task_3.txt', 'r') as input_file:
        for line in input_file:
            temp_inf = line.split()
            temp_personal = temp_inf[0]
            temp_salary = float(temp_inf[1])
            person_count += 1
            if temp_salary < 20000:
                min_salary_personal[temp_personal] = temp_salary
            average_salary += temp_salary
        average_salary = average_salary / person_count
    print('Результат обработки файла:\n '
          '\tСотрудники, чья ЗП < 20к:')
    for personal in min_salary_personal:
        print(f'\t\t{personal} - {min_salary_personal[personal]}')
    print(f'\tСредний доход сотрудников - {average_salary}')
except IOError:
    print('Ошибка при работе с фалами')
except TypeError:
    print('Ошибка! Неверно значение зарплаты указано в исходном файле. '
          'Допустимо использовать только цифры')
