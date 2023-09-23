from gtts import gTTS
import os
from tkinter import *
root = Tk()
canvas = Canvas(root,width=400,height=300)
canvas.pack()
def text_to_speech():
    text = entry.get()
    language = 'en'
    output = gTTS(text=text, lang=language, slow=False)
    output.save('fileoutput.mp4')
    os.system('start fileoutput.mp4')
entry = Entry(root)
canvas.create_window(200,180,window=entry)
button = Button(text="start",command=text_to_speech)
canvas.create_window(200,230,window=button)
root.mainloop()