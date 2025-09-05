import tkinter as tk
import random

target_number=None
attemps=0

def start_guess():
    global target_number,attemp
    target_number=random.randint(1,100)
    attemp=0
    lbl_result.config(text="Guess a number from 1 to 100")
    entry_co.delete(0,tk.END)
    lst_history.delete(0,tk.END)
def guess():
    global attemp
    try:
        user_input=int(entry_co.get())
    except ValueError:
        lbl_result.config(text='please enter a valid number')
        return
    attemps+=1
    if user_input>target_number:
        lbl_result.config(text='the number is smaller ')
        lst_history.insert(tk.END,f'try:{attemps}:{user_input} > target number')
    elif user_input<target_number:
        lbl_result.config(text='the number is larger ')
        lst_history.insert(tk.END,f'try:{attemps}:{user_input} < target number')
    else:
        lbl_result.config(text=f'Congratulations! you guessed in {attemp} tries ')
        lst_history.insert(tk.END,f'try:{attemps}:{user_input} is correct')
root=tk.Tk()
root.title('Number Guessing Game')
root.geometry('600x600')

main_font=('Segoe UI Emoji',12)

lbl_instruction=tk.Label(root,text='Take a guess',font=main_font)
lbl_instruction.pack(pady=10)

entry_co=tk.Entry(root,font=main_font)
entry_co.pack()

btn_guess=tk.Button(root,text='Guess',command=guess,font=main_font)
btn_guess.pack(pady=5)

btn_start=tk.Button(root,text='Reset',command=start_guess,font=main_font)
btn_start.pack(pady=5)

lbl_result=tk.Label(root,text='',font=main_font)
lbl_result.pack(pady=10)

lbl_history=tk.Label(root,text='history',font=main_font)
lbl_history.pack(pady=5)

lst_history=tk.Listbox(root,font=main_font,width=40,height=10)
lst_history.pack(pady=5)

start_guess()
root.mainloop()
#GG VanPhu 