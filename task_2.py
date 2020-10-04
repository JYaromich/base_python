def user_data(name: str, sur_name: str, birth_age: int,
              city: str, email: str, phone: str) -> None:
    """Функция выводит значение о пользователе

    :param name: имя
    :param sur_name: фамилия
    :param birth_age: год рождения
    :param city: город проживания
    :param email: электронный адрес
    :param phone: телефон
    :return: ничего не возвращает
    """

    print(f'Данные о пользователе:\n'
          f'Имя: {name}\n'
          f'Фамилия: {sur_name}\n'
          f'Год рождения: {birth_age}\n'
          f'Город проживания: {city}\n'
          f'Электронный адрес: {email}\n'
          f'Телефон: {phone}\n')


i_name = input('Введите ваше имя: ')
i_sur_name = input('Введите вашу фамилию: ')
while True:
    i_birth_age = input('Введите год рождения: ')
    if i_birth_age.isdecimal():
        i_birth_age = int(i_birth_age)
        break
    else:
        print('Ошибка! Введите корректный год рождения')
i_city = input('Введите ваш город проживания: ')
while True:
    i_email = input('Введите ваш электронный адрес: ')
    if i_email.count('@'):
        break
    else:
        print('Ошибка! Введен неверный электронный адрес')
while True:
    i_phone = input('Введите ваш номер телефона: ')
    if i_phone[0] == '+' and i_phone[1:len(i_phone)-1].isdigit():
        break
    else:
        print('Введите телофон в междунородном формате (+...)')
user_data(name=i_name, sur_name=i_sur_name, city=i_city, email=i_email,
          phone=i_phone, birth_age=i_birth_age)
