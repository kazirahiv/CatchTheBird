from tkinter import *
from HomeView import HomeView


root = Tk()

def on_closing():
    root.destroy()

HomeView(root=root)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()





