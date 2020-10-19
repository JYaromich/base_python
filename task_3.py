class Cell:
    @property
    def cells(self):
        return self.__cells

    @cells.setter
    def cells(self, cells):
        self.__cells = 0 if cells < 0 else cells

    def __init__(self, cells: int):
        self.cells = cells

    def __str__(self):
        return str(self.__cells)

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells - other.cells > 0:
            temp_cells = self.cells
            self.cells -= other.cells
            other.cells += temp_cells
            return self
        else:
            raise Exception("Ошибка! Разность ячеек меньше нуля")

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, number_of_row):
        counter = 0
        result = ''
        for _ in range(self.cells):
            counter += 1
            if counter == number_of_row:
                counter = 0
                result += '* \n'
            else:
                result += '*'
        return result


c1 = Cell(7)
c2 = Cell(4)
print(f'cells 1 - {c1}')
print(f'cells 2 - {c2}')
print(f'c1 + c2 - {c1 + c2}')
print(f'c1 * c2 - {c1 * c2}')
print(f'c1 / c2 - {c1 / c2}')
try:
    print(f'c1 - c2 - {c1 - c2}')
except Exception as e:
    print(e)
print(c1.make_order(2))
