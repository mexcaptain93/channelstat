class Filer():
    """Класс для ввода/вывода данных"""

    def __init__(self):
        pass

    def readfile(self, filename) -> list:
        with open(filename, 'r', encoding='utf8') as f:
            content = f.readlines()

        return content