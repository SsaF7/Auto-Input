import pyautogui
import time
import keyboard
from tkinter import messagebox

def entry(text, sec=0.1):
    print(f"\nЧерез 4 секунды начнется ввод текста")
    time.sleep(4)

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
    
    
    
    
    
    
    

if __name__ == "__main__":
    keyboard.on_press_key('esc', lambda e: stop_flag())
    file_data = open('datadata.txt', encoding='utf-8')
    data = file_data.read()
    delay = 0.1
    user_text = data
    print('Выбраный текст:')
    print(user_text)
    entry(user_text,delay)
    
