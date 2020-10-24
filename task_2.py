class DivZero(Exception):
    def __init__(self, txt='Деление на 0 невозможно, точнее сказать - это бесконечноть'):
        self.txt = txt


def dev(a: int, b: int) -> float:
    if b == 0:
        raise DivZero
    return a / b


try:
    print(dev(int(input('Введите числитель ')), int(input('Введите знаменатель '))))
except DivZero as de:
    print(de.txt)
