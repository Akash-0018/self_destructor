import tkinter as tk
from tkinter import ttk

class Selfdestructor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("You Stop Typing you'll Lose Your Work")

        self.text_label = ttk.Label(self, text="")
        self.text_label.pack(pady=75)

        self.entry = ttk.Entry(self)
        self.entry.pack()

        self.entry.bind("<KeyRelease>", self.on_key_release)
        self.entry.bind("<FocusOut>", self.clear_text)

        self.timer = None

    def on_key_release(self, event):
        if self.timer:
            self.after_cancel(self.timer)

        self.text_label.config(text=self.entry.get())
        self.timer = self.after(5000, self.clear_text)  

    def clear_text(self, event=None):
        self.text_label.config(text="")

if __name__ == "__main__":
    file = Selfdestructor()
    file.mainloop()