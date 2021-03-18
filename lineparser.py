import re
from datetime import datetime

from channel import Channel
from settings import settings


class LineParser():
    """Парсер строк"""

    def __init__(self):
        self.error = ''
        self.line = ''

    def parse(self, line):
        self.line = line
        self.error = ''
        time = self._gettime()
        name = 'Имя канала'
        # name = self._getName()
        status = self._getstatus()

        if self.error:
            print(f'{self.line}\r Строка не обработана! {self.error.strip()}')
            return False

        return Channel(name, time, status)

    def _gettime(self):
        time_str = re.search(r'\d{2}:\d{2}:\d{2}', self.line)
        if time_str:
            return time_str.group(0)
        else:
            self.error += 'Время не найдено! '

    def _getstatus(self):
        for up_maker in settings.up_markers:
            status_str = re.search(up_maker, self.line)
            if status_str:
                return "Up"

        for down_maker in settings.down_markers:
            status_str = re.search(down_maker, self.line)
            if status_str:
                return "Down"

        return 'Неизвестный статус'
