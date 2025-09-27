import pyautogui
import time
import keyboard
from tkinter import messagebox
import tkinter as tk
import threading



def entry(text, sec=0.1, time_wait=4):                              #основная функция программы
    time_wait_label.config(text=f"Через {time_wait} секунды начнется ввод текста", font=("Arial", 14))
    print(f"\nЧерез {time_wait} секунды начнется ввод текста")
    time.sleep(time_wait)
    time_wait_label.config(text='')
    for char in text:
        if flagstop[0]:
            messagebox.showinfo('Уведомление', 'Ввод принудительно завершён пользователем.')
            print('Ввод принудительно завершён пользователем')
            
            return
        
        if char == '\r\n':
            pyautogui.press("enter")
            time.sleep(sec * 2)
        else:
            keyboard.write(char)
            time.sleep(sec)
    messagebox.showinfo('Уведомление', 'Ввод завершён.')
    print(f"\nВвод завершен")

flagstop = [False]

def stop_flag():
    flagstop[0] = True
    
    
    
def naming():                                                                #функция после нажатии кнопки обраюатывает введенные значения и вызывает основную функцию
    user_text = ent.get('1.0','end').strip()
    if not user_text:
        messagebox.showinfo('Уведомление', 'Введите текст в поле.')
        return
    try:
        delay = float(delay_enter.get())
        start_delay = float(start_delay_enter.get())
    except ValueError:
        messagebox.showerror('Error', 'Введите корректные значения задержек (например 0.1 и 5)')
        return
    flagstop[0] = False
    threading.Thread(target=entry, args=(user_text,delay, start_delay), daemon=True).start() 
    
    
      
    
    
    
root = tk.Tk()
root.title('AutoEntry')
root.geometry("800x600")

label1 = tk.Label(root, text='Введите в поле текст', font=('Arial', 16))
label1.pack(padx=20)


label1 = tk.Label(root, text='Для принудительной остановки ввода нажмите ESC', font=('Arial', 10))
label1.pack(padx=10)


ent = tk.Text(root, height=10, width=40, font=("Arial", 12))
ent.pack(padx=60)



delay_frame = tk.Frame(root)
delay_frame.pack(pady=10, anchor="w", padx=20)


delay_label = tk.Label(delay_frame, text='Длина задержки ввода',font=('Arial', 12), anchor='w')  
delay_label.pack(side='left')
                  
delay_enter = tk.Entry(delay_frame, font=('Arial', 12), width=5,justify="left")
delay_enter.insert(0, "0.1")
delay_enter.pack(side='left',padx=107)
    
   
start_delay_frame = tk.Frame(root)
start_delay_frame.pack(pady=10, anchor='w', padx=20)   
   
    
start_delay_label = tk.Label(start_delay_frame, text='Задержка перед началом ввода',font=('Arial', 12),anchor='w') 
start_delay_label.pack(side='left')  

start_delay_enter = tk.Entry(start_delay_frame, font=('Arial', 12),justify="left",width=5)
start_delay_enter.insert(0, "4")
start_delay_enter.pack(side="left", padx=20)


butt = tk.Button(root, text = 'Начать ввод', font=('Arial', 25), command=naming)
butt.pack(pady=30)


time_wait_label = tk.Label(root,text='')
time_wait_label.pack(pady=10)
    



keyboard.on_press_key('esc', lambda e: stop_flag())
   
root.mainloop()