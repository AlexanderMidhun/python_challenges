from tkinter import *

import parser

root = Tk()
root.title("CALCULATOR")
display = Entry(root, width=20, font=('Arial', 14))
display.grid(row=1 , columnspan=6)

button_style = {'padx': 16, 'pady': 8, 'bd': 4, 'width': 2, 'font': ('Arial', 14)}

i=0
def get_variable(num):
    global i
    display.insert(i,num)
    i+=1

def clear_all():
    display.delete(0,END)

def undo():
    entire_string = display.get()
    if len(entire_string):
        new_string = entire_string[:-1]
        clear_all()
        display.insert(0,new_string)
    else:
        clear_all()
        display.insert(0,"Error")

def get_operation(opr):
    global i
    length =len(opr)
    display.insert(i,opr)
    i+=length


def calculate():
    entire_string = display.get()
    try:
        a = parser.expr(entire_string).compile()
        result = eval(a)
        clear_all()
        display.insert(0,result)
    except Exception:
        clear_all()
        display.insert(0,"error")



button = Button(root,text="1",**button_style,command=lambda :get_variable(1)).grid(row=2,column=0)
button = Button(root,text="2",**button_style,command=lambda :get_variable(2)).grid(row=2,column=1)
button = Button(root,text="3",**button_style,command=lambda :get_variable(3)).grid(row=2,column=2)

button = Button(root,text="4",**button_style,command=lambda :get_variable(4)).grid(row=3,column=0)
button = Button(root,text="5",**button_style,command=lambda :get_variable(5)).grid(row=3,column=1)
button = Button(root,text="6",**button_style,command=lambda :get_variable(6)).grid(row=3,column=2)

button = Button(root,text="7",**button_style,command=lambda :get_variable(7)).grid(row=4,column=0)
button = Button(root,text="8",**button_style,command=lambda :get_variable(8)).grid(row=4,column=1)
button = Button(root,text="9",**button_style,command=lambda :get_variable(9)).grid(row=4,column=2)

button = Button(root,text="0",**button_style,command=lambda :get_variable(0)).grid(row=5,column=0)
button = Button(root,text="+",**button_style,command=lambda :get_operation('+')).grid(row=5,column=1)
button = Button(root,text="-",**button_style,command=lambda :get_operation('-')).grid(row=5,column=2)

button = Button(root,text="/",**button_style,command=lambda :get_operation('/')).grid(row=6,column=0)
button = Button(root,text="*",**button_style,command=lambda :get_operation('*')).grid(row=6,column=1)
button = Button(root,text="%",**button_style,command=lambda :get_operation('%')).grid(row=6,column=2)

button = Button(root,text="%",**button_style,command=lambda :get_operation('%')).grid(row=2,column=4)
button = Button(root,text="exp",**button_style,command=lambda :get_operation('**')).grid(row=2,column=5)

button = Button(root,text="x!",**button_style).grid(row=3,column=4)
button = Button(root,text="^2",**button_style,command=lambda :get_operation('**2')).grid(row=3,column=5)

button = Button(root,text="(",**button_style,command=lambda :get_operation('(')).grid(row=4,column=4)
button = Button(root,text=")",**button_style,command=lambda :get_operation(')')).grid(row=4,column=5)

button = Button(root,text="=",**button_style,command=lambda :calculate()).grid(row=5,column=4)
button = Button(root,text="AC",**button_style,bg="red",command=lambda :clear_all()).grid(row=5,column=5)

button = Button(root,text="pi",**button_style,command=lambda :get_operation('3.14')).grid(row=6,column=4)
button = Button(root,text="->",**button_style,bg='#856ff8',command=lambda :undo()).grid(row=6,column=5)


root.mainloop()