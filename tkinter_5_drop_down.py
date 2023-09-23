from tkinter import *

def new_file():
    print("New File...")

def open_file():
    print("Open file......")

def save_file():
    print("Save File")

def settings_fun():
    print("Settings")

def recent_file():
    print("Recent files...")

def drop_bar():
    print("Executed")

def fun_cut():
    print("Cut...")

def fun_copy():
    print("Copy...")

def fun_next():
    print("Next...")

def fun_prev():
    print("Previous")

def fun_run():
    print("Run")

def fun_debug():
    print("Debug")

def fun_rename():
    print("Rename")

def fun_extract_method():
    print("Extract Method..")

root = Tk()

menu_bar = Menu(root)

#File
file_menu = Menu(menu_bar)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Save", command=save_file)
file_menu.add_command(label="settings", command=settings_fun)
file_menu.add_separator()
file_menu.add_command(label="recent files", command=recent_file)
file_menu.add_command(label="Exit", command=root.quit)

#Edit
edit_menu = Menu(menu_bar)
edit_menu.add_command(label="Cut", command=fun_cut)
edit_menu.add_command(label="Copy", command=fun_copy)
edit_menu.add_separator()
edit_menu.add_command(label="drop_bar", command=drop_bar)
edit_menu.add_command(label="drop_bar", command=drop_bar)
edit_menu.add_separator()
edit_menu.add_command(label="drop_bar", command=drop_bar)
edit_menu.add_command(label="drop_bar", command=drop_bar)


#Navigate
navigate_menu = Menu(menu_bar)
navigate_menu.add_command(label="Next", command=fun_next)
navigate_menu.add_command(label="Previous", command=fun_prev)
navigate_menu.add_separator()
navigate_menu.add_command(label="drop_bar", command=drop_bar)
navigate_menu.add_command(label="drop_bar", command=drop_bar)
navigate_menu.add_separator()
navigate_menu.add_command(label="drop_bar", command=drop_bar)
navigate_menu.add_command(label="drop_bar", command=drop_bar)

# Code
code_menu = Menu(menu_bar)
code_menu.add_command(label="Run", command=fun_run)
code_menu.add_command(label="Debug", command=fun_debug)
code_menu.add_separator()
code_menu.add_command(label="drop_bar", command=drop_bar)
code_menu.add_command(label="drop_bar", command=drop_bar)
code_menu.add_separator()
code_menu.add_command(label="drop_bar", command=drop_bar)
code_menu.add_command(label="drop_bar", command=drop_bar)

#Refactor
refactor_menu = Menu(menu_bar)
refactor_menu.add_command(label="Rename", command=fun_rename)
refactor_menu.add_command(label="Extract Method", command=fun_extract_method)
refactor_menu.add_separator()
refactor_menu.add_command(label="drop_bar", command=drop_bar)
refactor_menu.add_command(label="drop_bar", command=drop_bar)
refactor_menu.add_separator()
refactor_menu.add_command(label="drop_bar", command=drop_bar)
refactor_menu.add_command(label="drop_bar", command=drop_bar)

# cascading menus
menu_bar.add_cascade(label="File", menu=file_menu)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
menu_bar.add_cascade(label="Navigate", menu=navigate_menu)
menu_bar.add_cascade(label="Code", menu=code_menu)
menu_bar.add_cascade(label="Refactor", menu=refactor_menu)

root.config(menu=menu_bar)

toolbar = Frame(root,bg="#ffe225")
inbutton = Button(toolbar,text="crop")
inbutton.pack(side=LEFT,padx=2,pady=2)
toolbar.pack(side=TOP,fill=X)
statusbar = Label(root,text="This is Status",bd=2,anchor=W)
statusbar.pack(side=BOTTOM,fill=X)

root.mainloop()
