from pprint import pprint

try:
    subject_dict = {}
    with open('task_6.txt', 'r') as input_file:
        for line in input_file:
            subject_list = line.split()
            subject_dict[subject_list[0][:-1]] = sum(map(int, [subject[0:subject.index('(')] if subject.count('(') else
                                                               '0' for subject in subject_list]))
    pprint(subject_dict)

except IOError:
    print('Ошибка при работе с файлами')
except ValueError:
    print('Ошибка! Количество часов нужно указывать только цифрами')
