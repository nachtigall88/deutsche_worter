"""модуль для формування виконавчого інтерфейсу на tkinter"""
import tkinter as tk

root = tk.Tk()
root.title('DEUTSCHE WORTER')
root.geometry('800x500+60+20')
photo = tk.PhotoImage(file='germ.png')
root.iconphoto(False, photo)
root.config(bg='black')




if __name__ == '__main__':
    root.mainloop()