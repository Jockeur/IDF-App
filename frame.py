import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Passage du 2")
        self.geometry('720x480')
        self.background_color = '#D4D4D4'


        self._create_window()

    def _create_window(self):

        display_frame = tk.Frame(master=self, bg=self.background_color)
        display_frame.grid(row=0, column=0, sticky='nswe')
        display_frame.grid_columnconfigure(0, weight=1)
        display_frame.grid_columnconfigure(1, weight=1)

        