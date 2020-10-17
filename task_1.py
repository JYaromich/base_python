import time
from itertools import cycle


class TraficLight:
    _color = [['\x1b[0;31;41m' + '  ' + '\x1b[0m', 7],
              ['\x1b[0;33;43m' + '  ' + '\x1b[0m', 2],
              ['\x1b[0;32;42m' + '  ' + '\x1b[0m', 5],
              ['\x1b[0;33;43m' + '  ' + '\x1b[0m', 2]]

    def running(self):
        """
        Метод запускает работу светофора
        :return: None
        """
        for color in cycle(TraficLight._color):
            print(color[0])
            time.sleep(color[1])


tl = TraficLight()
tl.running()
