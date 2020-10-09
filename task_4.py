start_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print('Исходный список', start_list)
print(f'Конечный список: {[el for el in start_list if start_list.count(el) == 1]}')
