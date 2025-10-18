import tkinter as tk
from tkinter import ttk
from tkinter import * 

#=======================window settings
root = Tk()
root.title('Calculater')
root.geometry('400x600')
root.resizable(False,False)

#=======================grids
entry = tk.Entry(root, width=20, font=("Arial", 24), justify="right", bd=10, relief="sunken")
entry.grid(row=0, column=0, columnspan=4, pady=(20,10), padx=10, sticky="nsew")

#=======================click def
def click(btn_text):
    if btn_text == "=":
        try:
            result = str(eval(entry.get()))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

    elif btn_text == "C":
        entry.delete(0, tk.END)

    elif btn_text == "+-":    # <--- handle the toggle here
        current = entry.get()
        if current.startswith("-"):
            entry.delete(0)
        else:
            entry.insert(0, "-")

    else:
        entry.insert(tk.END, btn_text)

        
#=======================buttons
buttons = [
    ("C",1,0), ("()",1,1), ("%",1,2), ("/",1,3),
    ("7",2,0), ("8",2,1), ("9",2,2), ("*",2,3),
    ("4",3,0), ("5",3,1), ("6",3,2), ("-",3,3),
    ("1",4,0), ("2",4,1), ("3",4,2), ("+",4,3),
    ("+-",5,0), ("0",5,1), (".",5,2), ("=",5,3)
]

special_buttons = {}
special_buttons.update({ch: "white" for ch in "1234567890+-."})
special_buttons.update({ch: "green" for ch in "()%/*-+"})
special_buttons["C"] = "red"

for (text, r, c) in buttons:
    color = special_buttons.get(text, "black")
    btn = tk.Button(root, text=text, width=5, height=2,
                    fg=color, bg="lightgray", activebackground="cyan", activeforeground="white",
                    font=("Arial", 18), command=lambda t=text: click(t))
    btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
# تنظیم اندازه ردیف‌ها و ستون‌ها
for i in range(6):  # 1 تا 5 دکمه‌ها + ردیف 0 برای entry
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)
#=======================run
root.mainloop()