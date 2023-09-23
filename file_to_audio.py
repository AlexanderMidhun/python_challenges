from gtts import gTTS
import os
text = open('audio.txt','r').read()
language='en'
output = gTTS(text=text,lang=language,slow=False)
output.save('fileoutput.mp4')
os.system('start fileoutput.mp4')