from tkinter import *

root = Tk()
label = Label(root, text="Hello Midhun")
label.pack()
frame = Frame(root)
frame.pack()
button = Button(frame,text="OK")
button.pack()

root.mainloop()