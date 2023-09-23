from tkinter import *
from tkinter import messagebox

class ButtonActions:
    def __init__(self, root):
        self.root = root
        self.create_buttons()

    def create_buttons(self):
        button1 = Button(self.root, text="Button 1", command=self.show_message_clicked)
        button1.pack()

        button2 = Button(self.root, text="Button 2", command=self.show_message_cancel)
        button2.pack()

        button3 = Button(self.root, text="Button 3", command=self.exit_frame)
        button3.pack()

    def show_message_clicked(self):
        messagebox.showinfo("Clicked", "Button 1 clicked")
        print("Clicked")

    def show_message_cancel(self):
        messagebox.showinfo("Cancel", "Button 2 clicked")
        print("Cancel")

    def exit_frame(self):
        self.root.destroy()
        print("Exit")

root = Tk()
app = ButtonActions(root)
root.mainloop()
