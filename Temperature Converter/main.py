from tkinter import *
app = Tk()
app.geometry("700x400")
options = [1,2,3,4,5,6]
labe = OptionMenu(app, *options)
labe.pack()
app.mainloop()