class Channel():
    """Класс, описывающий канал"""

    def __init__(self, name, time, status):
        self.name = name
        self.time = time
        self.status = status

    def get_info(self):
        return f'{self.name} {self.time} {self.status}'