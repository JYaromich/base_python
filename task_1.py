class Matrix:
    def __init__(self, matrix: list):
        self.matrix = matrix

    def __str__(self):
        result_str = ''
        for m_list in self.matrix:
            for a in m_list:
                result_str += str(a) + '\t'
            result_str += '\n'
        return result_str

    def __add__(self, other):
        try:
            result_matrix = []
            for i in range(len(self.matrix)):
                temp_list = []
                for j in range(len(self.matrix[0])):
                    temp_list.append(self.matrix[i][j] + other.matrix[i][j])
                result_matrix.append(temp_list)
            return Matrix(result_matrix)
        except IndexError:
            print('Ошибка! Проверте совпадение порядков матрицы')


m1 = Matrix([[1, 2, 3], [3, 4, 5], [6, 7, 6]])
m2 = Matrix([[8, 6, 34], [23, 44, 65], [6, 7, 8]])
print(m1)
print(m2)
print(m1 + m2)
