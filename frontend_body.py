"""модуль для формування виконавчого інтерфейсу на tkinter"""
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('DEUTSCHE WORTER')
root.geometry('800x500+60+20')
photo = tk.PhotoImage(file='germ.png')
root.iconphoto(False, photo)
root.config(bg='black')

word_label2 = tk.Label(root, text='WORD', bg='black', fg='yellow', font=('Arial', 20, 'bold'), width=25, height=3)
word_label2.grid(row=2, column=1)
click_button = tk.Button(root, text='CLICK', bg='red', fg='black', font=('Arial', 20, 'bold'), width=10, height=1)
click_button.grid(row=2, column=2)
hint_combobox = ttk.Combobox(root, values=[' ', 'article', 'my hint'])
hint_combobox.current(0)
hint_combobox.grid(row=3, column=1)
frame = tk.LabelFrame(root, text='isert data', bg='yellow')
frame.grid(row=6, column=1)
art_entry = tk.Entry(frame, width=20)
art_entry.grid(row=0,column=1)
word_entry = tk.Entry(frame, width=10)
word_entry.grid(row=0,column=2)
transl_entry = tk.Entry(frame, width=10)
transl_entry.grid(row=0,column=3)
insert_button = tk.Button(frame, text='INSERT',bg='black',fg='yellow')
insert_button.grid(row=6, column=3)

if __name__ == '__main__':
    root.mainloop()
