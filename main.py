
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from textes import textes
import random

#--------------------For functions--------------
x=0
score=0
written_text=""
timer=None
correct_letters=""
missed_letters=""
#text as list
textes=textes
copy_texts=None
#---------------
#TAKE THE BEST RESULT EVER
with open('best_result.txt','r') as file:
    best_score=float(file.read())
print(best_score)
#-----------------------------------------------


def start():
    global score,list_of_words,timer,textes
    copy_texts = textes
    score=0
    list_of_words = random.choice(copy_texts)
    background_text()

def background_text():
    global text, list_of_words, label_rules,score_label,score,correct_letters,missed_letters
    #reload game
    correct_letters=''
    missed_letters=""
    score=0
    score_label.config(text=f"Score: {score}", font=('Courier', 16, 'normal'))
    written_text = ""
    for i, word in enumerate(list_of_words):
        written_text += word + " "

        # Check if 15 words have been added or if it's the last word
        if (i + 1) % 15 == 0 or i == len(list_of_words) - 1:
            written_text += "\n"  # Start a new line
    label_rules.config(text=written_text)
    label_rules.grid(row=0,column=0)
    start_timer(60)

def start_timer(count):
    global score,best_score,timer
    if timer is not None:
        window.after_cancel(timer)
    count_sec = count % 61
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    timer_label.config(text=f"TIMER:\n\n"
                          f"{count_sec} seconds",font=('Courier',16,'normal'),bg='#FFE4D6')
    if count > 0:
        # global timer
        timer = window.after(1000, start_timer, count - 1)
    else:
        # print(correct_letters)
        total_key_pressed = len(correct_letters) + len(missed_letters)
        WPM = (total_key_pressed / 5) / 1
        if score > best_score:
            with open('best_result.txt','w') as file:
                file.write(str(WPM))

        accuracy=len(correct_letters)/total_key_pressed * 100
        messagebox.showinfo(title="FINISH", message=f"Time is done!\nYour score: {score}\n"
                                                    f"Correct letters: {len(correct_letters)} and missed: {len(missed_letters)}\n"
                                                    f"Your Type Speed is: {round(WPM,2)}WPM\n"
                                                    f"With {accuracy}% accuracy")

    # global timer
    # count_sec = count % 60
    # if count_sec < 10:
    #     count_sec = f"0{count_sec}"

def get_entry(event):
    #spacebar triggered
    global entry,x, list_of_words,written_text,score,correct_letters,missed_letters,textes
    written_text = ""
    text=entry.get().lower()
    entry.delete(first=0,last=len(text)) # 0,END
    text_no_space=text.strip()
    # print(len(list_of_words[x]))
    if text_no_space==list_of_words[x]  :
        # print("correct")
        score += 1
        score_label.config(text=f"Score: {score}", font=('Courier', 16, 'normal'))
        # print(f"Score: {score}")
        correct_letters += list_of_words[x]
        del list_of_words[x]
    else:
        # print('not correct')
        missed_letters += text_no_space
        del list_of_words[x]
        # for _ in list_of_words:
        #     if _ == text_no_space:
        #         written_text= written_text + "GREAT"
        #     else:
        #         written_text = written_text + "bad"
        # # written_text= written_text
    for i, word in enumerate(list_of_words):
        written_text += word + " "

        # Check if 15 words have been added or if it's the last word
        if (i + 1) % 15 == 0 or i == len(list_of_words) - 1:
            written_text += "\n"  # Start a new line

    if len(list_of_words) < 2:
        list_of_words = random.choice(textes)
        for _ in list_of_words:
            written_text += _ + " "
    label_rules.config(text=written_text)

def get_entry_1():
    global entry,x, list_of_words,written_text,score,correct_letters,missed_letters,textes
    written_text = ""
    text=entry.get().lower()
    entry.delete(first=0,last=len(text))
    text_no_space = text.strip()
    if text_no_space == list_of_words[x]:
        score+=1
        score_label.config(text=f"Score: {score}", font=('Courier', 16, 'normal'))
        correct_letters += list_of_words[x]
        del list_of_words[x]
    else:
        missed_letters += text_no_space
        del list_of_words[x]
    for i, word in enumerate(list_of_words):
        written_text += word + " "
        if (i + 1) % 15 == 0 or i == len(list_of_words) - 1:
            written_text += "\n"

    if len(list_of_words) < 2:
        list_of_words = random.choice(textes)
        for _ in list_of_words:
            written_text += _ + " "
    label_rules.config(text=written_text)
#--------MAIN-------
window=tk.Tk()
window.title("Text Writing Speed Test")
window.minsize(1024,720)
window.config(bg='#FFE4D6',pady=50,padx=50)

#FRAMES
top_frame=tk.Frame(window,height=50,width=400)
top_frame.grid(row=0,column=1)

middle_frame=tk.Frame(window,height=400,width=520,pady=100,)
middle_frame.grid(row=2,column=1)
#ENTRY
entry=tk.Entry(width=50)
entry.focus()
entry.grid(row=3,column=1,pady=20)
#LABELS
text="Type words in entry below. Before start tap the button 'PLAY NOW'.\n You can use spacebar or button to go to the next word"
label_rules=tk.Label(middle_frame,text=text)
label_rules.grid(row=0,column=1)

title_label=tk.Label(top_frame,text="Typing Speed Test", font=('Courier',26,'bold'))
title_label.pack()

score_label=tk.Label(middle_frame,text=f"", font=('Courier',16,'normal'))
score_label.grid(row=1,column=0)

time=60
timer_label=tk.Label(text=f"TIMER:\n\n"
                          f"{time} seconds",font=('Courier',16,'normal'),bg='#FFE4D6')
timer_label.grid(row=2,column=0)

best_result_label=tk.Label(text=f"Best result: {best_score}\n words per minute")
best_result_label.grid(row=3,column=0)
#try on the rules
list_of_words=text.lower().split()
#Buttons
start_pillow_image=Image.open("Image.png")
start_pillow_image=start_pillow_image.resize((36*4,9*4))
start_button_image=ImageTk.PhotoImage(start_pillow_image)
start_button=tk.Button(image=start_button_image,command=start,highlightthickness=0,background="#FFE4D6")
start_button.grid(row=4,column=1)

space_button=tk.Button(text="spacebar",command=get_entry_1,width=30)
space_button.grid(row=5,column=1,pady=20)
window.bind("<space>",get_entry)





window.mainloop()


