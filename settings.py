class Settings():
    """Параметры"""

    def __init__(self):
        self.input_file = 'input.txt'
        self.up_markers = [
            'Установлено соединение с СТМ',
            ' работает	нет',
            'Восстановлено соединение с'
        ]
        self.down_markers = [
            ' не работает.',
            'Нет соединения с СТМ',
        ]


settings = Settings()