from playsound import playsound 
from gtts import gTTS
from tkinter import *
from tkinter import messagebox
import os
def texttosound():
    text = textinput.get()
    if text.strip():
        text = gTTS(text=text, lang='en')
        audio_file = "output.mp3"
        text.save(audio_file)
        playsound(audio_file)
        os.remove(audio_file)
    else:
        messagebox.showerror(title="No text entered!",message="No text entered!")

def reset():
    textinput.delete(0,END)

frame=Tk()
frame.geometry("520x500")
frame.title("Text to Speech")
label=Label(frame,text="Text To Speech Project",font="Times 20")
label.grid(row=0,column=1)
label2=Label(frame,text="Enter your Text : ",font="Helvetica 15").grid (row=2,column=0)
textinput=Entry(frame,width=30)
textinput.focus()
textinput.grid(row=2,column=1,pady=40)

start=Button(frame,text="Start",command=texttosound,bg="#ccc",font="Arial 15 ",pady=10,padx=20).grid(row=3,column=0)

exit=Button(frame,text="Exit",command=frame.destroy,bg="red",font="Arial 15 ",pady=10,padx=20).grid(row=3,column=1)

start=Button(frame,text="Reset",command=reset,bg="blue",font="Arial 15 ",pady=10,padx=20).grid(row=3,column=2)

frame.mainloop()
# mohmed fetoh ragab
