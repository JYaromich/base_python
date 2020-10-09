from sys import argv

try:
    wages = float(argv[1]) * float(argv[2])
    print(f'ЗП = { wages + wages * (int(argv[3]) / 100):.2f}')
except ValueError:
    print('В качестве параметров необходимо передовать только цифры')
except IndexError:
    print('Для корректной работы программы в качетсве аргументов передайте: '
          'количество отработанного времени работником, стоимость одного часа работника, '
          'премия в %')
