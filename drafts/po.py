import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title('AutoEntry')
root.geometry("800x600")

label1 = tk.Label(root, text='Введите в поле текст', font=('Arial', 16))
label1.pack(padx=20)

ent = tk.Text(root, height=20, width=30, font=("Arial", 12))
ent.pack()

def naming():
    user_text = ent.get('1.0','end')
    
    
    

butt = tk.Button(root, text = 'Начать ввод', font=('Arial', 25), command=naming)
butt.pack(pady=50)

timer = tk.Label(root, text = '', font=("Arial", 14))

root.mainloop()