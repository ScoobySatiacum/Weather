import tkinter as tk
from app import App

root = tk.Tk()
root.title('Weather')
root.configure(background='black')
myapp = App(root)
myapp.mainloop()