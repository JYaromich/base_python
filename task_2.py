from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def length_cloth(self):
        pass


class Suit(Clothes):
    @property
    def h(self):
        return self.__h

    @h.setter
    def h(self, h):
        self.__h = 100 if h < 100 else h

    def __init__(self, h: int):
        self.h = h

    def length_cloth(self):
        return 2 * self.h + 0.3


class Coat(Clothes):
    @property
    def v(self):
        return self.__v

    @v.setter
    def v(self, v):
        self.__v = 46 if v < 46 else v

    def __init__(self, v: int):
        self.v = v

    def length_cloth(self):
        return self.v / 0.65 + 0.5


coat = Coat(0)
suit = Suit(175)
print(f'{round(coat.length_cloth(), 2)}')
print(f'{round(suit.length_cloth(), 2)}')