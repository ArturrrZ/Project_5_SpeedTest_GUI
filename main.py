
import tkinter as tk
from PIL import Image, ImageTk, ImageFilter, ImageEnhance

window=tk.Tk()
window.title("Text Writing Speed Test")
window.minsize(1024,720)
window.config(bg='#FFE4D6',pady=50,padx=50)
#INVISIBLE TO HELP ME WITH GRID
invisible_l_1=tk.Label(text="",background="#FFE4D6",padx=90)
invisible_l_1.grid(row=1,column=0)
#FRAMES
top_frame=tk.Frame(window,height=50,width=400)
top_frame.grid(row=0,column=1)

middle_frame=tk.Frame(window,height=400,width=520,pady=100,)
middle_frame.grid(row=2,column=1)

entry=tk.Entry(width=70,)
entry.grid(row=3,column=1,pady=20)

start_pillow_image=Image.open("Image.png")
print(start_pillow_image.size)
start_pillow_image=start_pillow_image.resize((36*4,9*4))
print(start_pillow_image.size)
start_button_image=ImageTk.PhotoImage(start_pillow_image)
# start_pillow_image.resize(())

def start():

    pass



def background_text():
    global text, list_of_words, label_rules

    for _ in list_of_words:
        print(_)
        _

x=0
written_text=""
def get_entry(event):
    global entry,x, list_of_words,written_text
    written_text = ""
    text=entry.get()
    entry.delete(first=0,last=len(text))
    text_no_space=text.strip()
    print(len(list_of_words[x]))
    if text_no_space==list_of_words[x]  :
        print("correct")
        list_of_words[x]="GREAT"
    else:
        print('not correct')
        list_of_words[x] = "bad"
        # for _ in list_of_words:
        #     if _ == text_no_space:
        #         written_text= written_text + "GREAT"
        #     else:
        #         written_text = written_text + "bad"
        # # written_text= written_text
    for _ in list_of_words:
        written_text += _ + " "

    label_rules.config(text=written_text)
    # print(written_text)
    print(list_of_words)
    print(len(text))
    print(f"Original text: {list_of_words[0]}\nYou typed: {text}\nTheir types: {type(list_of_words[0])} and {type(text)}")
    x+=1
def get_entry_1():
    global entry
    text=entry.get()
    entry.delete(first=0,last=len(text))
    print(text)

start_button=tk.Button(image=start_button_image,command=background_text,highlightthickness=0,background="#FFE4D6")
start_button.grid(row=4,column=1,)

space_button=tk.Button(text="space",command=get_entry_1)
space_button.grid(row=5,column=1,pady=20)
window.bind("<space>",get_entry)

text="Type words in entry below Before start tap the button PLAY NOW"
list_of_words=text.lower().split()
print(list_of_words)
label_rules=tk.Label(middle_frame,text=text)
label_rules.place(x=100,y=100)


window.mainloop()


