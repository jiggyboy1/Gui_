import tkinter as tk
import random


root = tk.Tk()
root.config(bg="indigo")

root.title('Random Guess Game')
root.geometry('450x250')


entry = tk.Entry(root,width=40,border=5)
entry.pack(padx=5,pady=5)

rand_num = random.randint(1,10)
def myOnclick():
    show_number = entry.get()
    global entry_val
    entry_val = int(show_number)
    hint = ""
    if entry_val > rand_num:
        hint = " Go lower"
    else:
        hint = " Go higher"

    if entry_val > rand_num:
        msg.configure(text=str(entry_val) + " Too High " + hint)
    elif entry_val <rand_num:
        msg.configure(text=str(entry_val) + " Too Low " + hint)
    else:
        msg.configure(text="Correct! ")


def myclear():
    entry.delete(0,tk.END)


label = tk.Label(root,text="Guess a number",font=("helvetica",15,"bold"))
label.pack()

button = tk.Button(root,text="Sumbit Your name",command=myOnclick,padx=5,pady=0)
button.pack()

button2 = tk.Button(root,text="Clear",command=myclear,)
button2.pack()

msg = tk.Label(root,text="")
msg.pack()

root.mainloop()