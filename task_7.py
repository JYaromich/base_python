class ComplexNumber:
    def __init__(self, real_part: int, fictional_part: int):
        self.fictional_part = fictional_part
        self.real_part = real_part

    def __mul__(self, other):
        return ComplexNumber(self.real_part * other.real_part - self.fictional_part * other.fictional_part,
                             self.real_part * other.fictional_part + self.fictional_part * other.real_part)

    def __add__(self, other):
        return ComplexNumber(self.real_part + other.real_part, self.fictional_part + other.fictional_part)

    def __str__(self):
        return f"{self.real_part}{'+' + str(self.fictional_part) if self.fictional_part > 0 else self.fictional_part}i"


a = ComplexNumber(2, 3)
b = ComplexNumber(-1, 1)
print(a)
print(b)
print(a + b)
print(a * b)
