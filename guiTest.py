#!/usr/bin/python
# -*- coding: utf-8 -*-

from Tkinter import Tk, W, E
from ttk import Frame, Button, Label, Style
from ttk import Entry


class Example(Frame):
  
    def __init__(self, parent):
        Frame.__init__(self, parent)   
         
        self.parent = parent
        
        self.initUI()
        
    def initUI(self):
      
        self.parent.title("Find inside video")
        
        Style().configure("TButton", padding=(0, 5, 0, 5), 
            font='serif 10')
        
        self.columnconfigure(0, pad=3)
        self.columnconfigure(1, pad=3)
        self.columnconfigure(2, pad=3)
        self.columnconfigure(3, pad=3)
        
        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3)
        self.rowconfigure(2, pad=3)
        self.rowconfigure(3, pad=3)
        self.rowconfigure(4, pad=3)
        
        entry = Entry(self)
        entry.grid(row=0, columnspan=4, sticky=W+E)
        
        bck = Button(self, text="Next")
        bck.grid(row=1, column=1)
        lbl = Button(self, text="Previous")
        lbl.grid(row=1, column=2)    
        
        
        self.pack()

def main():
  
    root = Tk()
    app = Example(root)
    root.mainloop()  


if __name__ == '__main__':
    main() 