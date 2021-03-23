class Event():
    """Класс, описывающий канал"""

    def __init__(self, name, time, status, object):
        self.name = name
        self.time = time
        self.status = status
        self.object = object

    def get_info(self):
        return f'{self.name} {self.object} {self.time} {self.status}'