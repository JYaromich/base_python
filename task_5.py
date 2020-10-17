class Stationery:
    def __init__(self, title: str):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Рисует {self.title} тонко')


class Pencil(Stationery):
    def draw(self):
        print(f'Рисует {self.title} серым')


class Handle(Stationery):
    def draw(self):
        print(f'Рисует {self.title} оранжевым')


stationery = Stationery('Stationery')
pen = Pen('Ручка')
pencil = Pencil('Карандаш')
handle = Handle('Маркер')
stationery.draw()
pen.draw()
pencil.draw()
handle.draw()
