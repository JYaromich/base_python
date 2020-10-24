class OnlyNumberException (Exception):
    def __init__(self, txt="Ошибка! Вводить нужно только числа"):
        self.txt = txt

    def __str__(self):
        return self.txt


result = []
while inputNum := input('Для выхода из программы введите stop. \nВведиет число '):
    if inputNum == 'stop':
        break

    try:
        if not inputNum.isdecimal():
            raise OnlyNumberException
        result.append(int(inputNum))
    except OnlyNumberException as err:
        print(err)
print(f'Результат: {result}')
