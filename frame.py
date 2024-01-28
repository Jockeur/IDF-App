import tkinter as tk
import logic

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Passage du 2")
        self.geometry('720x480')
        self.background_color = '#D4D4D4'

        self.passage_label_text = tk.StringVar()

        self.timer = logic.Timer('data.json')
        self.requester = logic.Requester('data.json')

        self.requester.request_next_passage('419093', 'C00553')
        self.timer.get_bus_time()

        self._create_window()

    def _create_window(self):

        display_frame = tk.Frame(master=self, bg=self.background_color)
        display_frame.grid(row=0, column=0, sticky='nswe')

        self.passage_label_text.set(f'Le bus 2 passe dans {self.timer.get_difference()} minutes à l\'arrêt "Les Bordes"')
        passage_label = tk.Label(display_frame, textvariable=self.passage_label_text)
        passage_label.grid(master=display_frame,
                            row=0,
                            column=0,
                            sticky='nswe')
        
    def update_time(self, label: tk.Label, stop_point_id: str, line_id: str):
        self.requester.request_next_passage(stop_point_id, line_id)
        self.timer.get_bus_time()
        self.passage_label_text.set(f'Le bus 2 passe dans {self.timer.get_difference()} minutes à l\'arrêt "Les Bordes"')
        self.update_idletasks()