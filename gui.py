import tkinter as tk
import tkinter.ttk as ttk

class GUI():
    """Класс для графического интерфейса"""

    def __init__(self, function):

        window = tk.Tk()
        window.title("Парсер событий")
        heading = tk.Label(text="Парсер событий")
        text_box = tk.Text(
            width=160,
            height=16
        )
        but = tk.Button(text="Старт!")

        but.bind('<Button-1>', function)


        heading.pack()
        text_box.pack()
        but.pack()
        window.mainloop()

