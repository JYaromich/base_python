class Worker:
    def __init__(self, name: str, surname: str, position: str, income: dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income
        #


class Position(Worker):
    def get_full_name(self):
        return f'Full name: {self.name} {self.surname}'

    def get_total_income(self):
        return f"Total Income " \
               f"{self._income.get('wage') +  self._income.get('bonus')}"


bob = Position('Bob', 'Gray', 'engineer', {'wage': 5000, 'bonus': 1000})
anna = Position('Anna', 'Red', 'actor', {'wage': 6000, 'bonus': 10000})
print(bob.get_full_name())
print(bob.get_total_income())
print(anna.get_full_name())
print(anna.get_total_income())
