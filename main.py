from settings import settings
from filer import Filer
from lineparser import LineParser


class ChannelStat():
    """Главный класс"""

    def __init__(self):
        self.filer = Filer()
        self.events = self.get_events()
        self.parser = LineParser()

        for event in self.events:
            channel = self.parser.parse(event)
            if channel:
                print(channel.get_info())

    def get_events(self):
        try:
            channels = self.filer.readfile(settings.input_file)
        except FileNotFoundError:
            print(f'Нет такого файла {settings.input_file}')
            return False

        self.filer.writefile(settings.output_file)

        return channels


if __name__ == '__main__':
    app = ChannelStat()

