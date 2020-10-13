ru = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

try:
    translate_lines = []
    with open('task_4.txt', 'r') as input_file:
        for line in input_file:
            translate_words = ' '.join([word if not ru.get(word) else ru.get(word) for word in line.split()]) + '\n'
            translate_lines.append(translate_words)
    with open('new_task4.txt', 'w') as output_file:
        output_file.writelines(translate_lines)
except IOError:
    print('Ошибка при работе с файлами')
