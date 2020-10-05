def int_func(word: str) -> str:
    """
    Функция принимает строку состоящую из маленьких латинских букв и возвращает слово, начинающееся с большой буквы
    :param word: слово из латинских букв
    :return: слова с первой большой буквы или False в случае, если слово состояит не из латинских букв
    """
    latin_char = frozenset('qwertyuiopasdfghjklzxcvbnm')
    return word.title() if not set(word).difference(latin_char) else False


words = input('Введите строку из слов разделнных пробелом: ').split()
for word in words:
    result = int_func(word)
    if result:
        print(int_func(word), ' ')
