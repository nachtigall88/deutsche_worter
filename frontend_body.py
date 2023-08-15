"""модуль для формування виконавчого інтерфейсу на tkinter"""
import tkinter as tk
from tkinter import ttk


def rule_entries():
    """
    функція для ввімкнення/вимкнення ентрі-полів для вводу інформації ""
    :return:
    """
    for i in [art_entry, word_entry, transl_entry]:
        if varint.get() == 1:
            i.config(state='normal')
        else:
            i.config(state='disabled')


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
frame = tk.LabelFrame(root, text='isert data', fg='yellow', bg='black')
frame.grid(row=7, column=1)
empty_label = tk.Label(text='empty data', bg='black', fg='black', height=5)
empty_label.grid(row=6, column=1)
art_entry = tk.Entry(frame, width=9, state='disabled')
art_entry.grid(row=0, column=1)
word_entry = tk.Entry(frame, width=20, state='disabled')
word_entry.grid(row=0, column=2)
transl_entry = tk.Entry(frame, width=20, state='disabled')
transl_entry.grid(row=0, column=3)
insert_button = tk.Button(frame, text='INSERT', bg='black', fg='yellow')
insert_button.grid(row=6, column=3)
varint = tk.IntVar()
enabler = tk.Checkbutton(root, text='enable/disable', bg='black', fg='red', activebackground='black',
                         activeforeground='red', offvalue=0, onvalue=1, variable=varint, command=rule_entries)

enabler.grid(row=7, column=2)

if __name__ == '__main__':
    root.mainloop()
