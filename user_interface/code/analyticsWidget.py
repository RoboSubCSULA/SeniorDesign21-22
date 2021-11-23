import tkinter as tk
import tkinter.font as tkFont

class AnalyticsWidget(tk.Frame):
    def __init__(self, parent, title, data, width, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.data = data
        self.switch = True
        self.title = tk.Label(master=self, text=title, width=width, pady=5,  bg='#d8e7e8')
        self.title.pack(fill='both')

        fontStyle = tkFont.Font(family='Lucida Grande', size=15)
        self.info = tk.Label(master=self, text=self.data, font=fontStyle, width=width, pady=25)

        self.info.pack()


    def update(self, new_data):
        self.data = new_data
        self.info.config(text = self.data)
