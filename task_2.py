first_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(f'Иcходный список: {first_list}')
print(f'Преобразованный список: {[el for i, el in enumerate(first_list[1:]) if el > first_list[i]]}')

