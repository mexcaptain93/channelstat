import re
from datetime import datetime

from event import Event
from settings import settings


class LineParser():
    """Парсер строк"""

    def parse(self, line):
        self.error = ''
        self.line = line

        regex_main = r"(?P<datetime>\d+\.\d+\.\d+ \d+\:\d+\:\d+)\t(?P<data>.+?)\t(?P<object>.+?)\t(?P<info2>.+?)\n"
        regex_name = r"\((.*)\)"

        match = re.search(regex_main, self.line, re.MULTILINE | re.IGNORECASE)

        if match:
            time = match.group('datetime')
            object = match.group('object')

            name_match = re.search(regex_name, match.group('data'))

            if name_match:
                name = name_match.group(1) # Без скобок
        else:
            self.error = f'Строка не обработана! {self.line}'

        status = self._getstatus()

        if self.error:
            print(self.error)
            return False

        return Event(name, time, status, object)


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
