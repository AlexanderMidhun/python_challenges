from tkinter import *

root = Tk()
user_name = Label(root, text="User Name")
mob = Label(root,text="Mobile Number")
email = Label(root, text="Email")
age = Label(root, text="age")
password = Label(root, text="Password")
confirm_password = Label(root, text="Confirm Password")
entry1 = Entry(root)
entry2 = Entry(root)
entry3 = Entry(root)
entry4 = Entry(root)
entry5 = Entry(root)
entry6 = Entry(root)
login = Button(text="LOGIN")
cancel = Button(text="CANCEL")

user_name.grid(row=0,column=0)
entry1.grid(row=0,column=1)
mob.grid(row=1,column=0)
entry2.grid(row=1,column=1)
email.grid(row=2,column=0)
entry3.grid(row=2,column=1)
age.grid(row=3,column=0)
entry4.grid(row=3,column=1)
password.grid(row=4,column=0)
entry5.grid(row=4,column=1)
confirm_password.grid(row=5,column=0)
entry6.grid(row=5,column=1)
login.grid(row=6,column=0)
cancel.grid(row=6,column=1)

root.mainloop()


