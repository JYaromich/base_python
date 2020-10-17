class Road:
    def __init__(self, lenght: float, width: float):
        """
        Конструктор класса Road
        :param lenght: Длина асфальта, m
        :param width: Ширина асфальта, m
        """
        self._lenght = lenght
        self._width = width

    def mass(self):
        """
        Метод расчета массы асфальта
        :return: Значение массы (float)
        """
        return self._width * self._lenght * 25 * 5 / 1000


print(f'Масса асфальта необходимого для покрытия = '
      f'{Road(5000, 20).mass()} т')
