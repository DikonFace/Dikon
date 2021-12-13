from tkinter import *
import sqlite3

window = Tk()
window.geometry("400x400")
window.minsize(width=400, height=400)
window.maxsize(width=400, height=400)

def conacona():
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS stud (firstname TEXT, secondname TEXT)")
    conn.commit()
    conn.close()

def main_frame(window):

    display_main = Frame(window, width=400, height=400)
    display_main.place(x=200, y=200, anchor=CENTER)

    button_reg = Button(display_main, text='регистрация', command=lambda window = window: reg_frame(window))
    button_reg.place(x=200, y=200, anchor=CENTER)

    button_log = Button(display_main, text='Войти', command=lambda window = window: log_frame(window))
    button_log.place(x=200, y=150, anchor=CENTER)

def log_frame(window):
    #переменные
    
    #функции
    conn = sqlite3.connect('student.db')
    c = conn.cursor()
    c.execute('SELECT * FROM stud')
    rows = c.fetchall()
    conn.commit()
    conn.close()

    #виджеты и т.д.
    display_log = Frame(window, width=400, height=400)
    display_log.place(x=200, y=200, anchor=CENTER)
    test = Label(log_frame, text=rows)
    test.place(x=50, y=50, anchor=CENTER)
    buttontest = Button(display_log)
    buttontest.place(x=200, y=200, anchor=CENTER)


def reg_frame(window):
    # переменные 
    firstname_entry = StringVar()
    secondname_entry = StringVar()

    # функции
    def display_destroy():
        display_reg.destroy()

   

    # виджеты
    
    display_reg = Frame(window, width=400, height=400)
    display_reg.place(x=200, y=200, anchor=CENTER)

    firstname_label = Label(display_reg, text="Name")
    firstname_label.place(x=200, y=50, anchor=CENTER)
    firstname_entry_entry = Entry(display_reg, textvariable=firstname_entry)
    firstname_entry_entry.place(x=200, y=75, anchor=CENTER)

    secondname_label = Label(display_reg, text="Password")
    secondname_label.place(x=200, y=125, anchor=CENTER)
    secondname_entry_entry = Entry(display_reg, textvariable=secondname_entry)
    secondname_entry_entry.place(x=200, y=150, anchor=CENTER)

    def huinyah():
        print("имя пользователя" + " " +  firstname_entry.get())
        print("Введенный пароль" + " " + secondname_entry.get())
        print(dir(firstname_entry))
        conn = sqlite3.connect('student.db')
        c = conn.cursor()
        c.execute('INSERT INTO stud (firstname, secondname) VALUES (?,?)', (firstname_entry.get(), secondname_entry.get()))
        conn.commit()
        print("OK")

    button_back = Button(display_reg, text='back', command=display_destroy)
    button_back.place(x=200, y=175, anchor=CENTER)

    button_enter = Button(display_reg, text="enter", command=huinyah)
    button_enter.place(x=200, y=200, anchor=CENTER)




conacona()
main_frame(window)
window.mainloop()