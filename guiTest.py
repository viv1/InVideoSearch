import Tkinter as tk

class FindGUI(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Find inside video")

        self.entry = tk.Entry(self)
        self.button1 = tk.Button(self, text="Search", command=self.on_button)
        self.button2 = tk.Button(self, text="Next", command=self.on_button)
        self.button3 = tk.Button(self, text="Previous", command=self.on_button)


        self.entry.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()


    def on_button(self):
        return (self.entry.get())

