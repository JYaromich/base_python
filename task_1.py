class DateError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Date:
    def __init__(self, date):
        self.day, self.month, self.year = self.read_data(date)

    @classmethod
    def read_data(cls, date: str):
        try:
            result = tuple(map(int, date.split('-')))
            cls.validation_date(*result)
            return result
        except DateError as dr:
            raise dr

    @staticmethod
    def validation_date(date, month=None, year=None):
        if 0 < date > 31:
            raise DateError("Ошибка! Неверно задан день. Должно быть от 1 до 31")

        if month:
            if 0 < month > 12:
                raise DateError("Ошибка! Неверно задан месяц. Должно быть от 1 до 12")
        elif year:
            if year < 0:
                raise DateError('Ошибка! Неверно задан год. Должно быть больше 0')


try:
    d = Date("12-10-2020")
    print(f'Число - {d.day} Месяц - {d.month} Год - {d.year}')
except DateError as dr:
    print(dr.txt)
