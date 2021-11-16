import tkinter
from tkinter import ttk
from tkinter import END
v = 0


def v_sfery():
    global v
    try:
        if int(entry.get()) > 0:
            v = 4 / 3 * 3.14 * (int(entry.get()) ** 3)
            entry2.delete(0, END)
            entry2.insert(0, v)
        else:
            entry2.delete(0, END)
            entry2.insert(0, 'Неверное значение радиуса!')
    except ValueError:
        entry2.delete(0, END)
        entry2.insert(0, 'Неверное значение радиуса!')


def save():
    if str(tip.get()) == 'Текст':
        with open('Объем сферы.txt', 'w') as s_f:
            s_f.write(str(v))
    elif str(tip.get()) == 'HTML':
        with open('Объем сферы.html', 'w', encoding='utf-8') as s_f:
            s_f.write("<html>"
                      + "\n"
                      + "<head>"
                      + "\n"
                      + "<meta charset='utf-8'>"
                      + "\n"
                      + "</head>"
                      + "\n"
                      + "<body>"
                      + "\n"
                      + "<p>"
                      + "\n"
                      + str(v)
                      + "\n"
                      + "</p>"
                      + "\n"
                      + "</body>"
                      + "\n"
                      + "</html>")
    else:
        entry2.delete(0, END)
        entry2.insert(0, 'Ошибка!')


window = tkinter.Tk()
window.geometry('500x200')
frame = tkinter.Frame()
frame.grid(row=4, column=2)
label = tkinter.Label(frame, text='Программа вычисления объема сферы')
label.grid(row=0, column=1)
label1 = tkinter.Label(frame, text='Введите радиус:')
label1.grid(row=1, column=0)
entry = tkinter.Entry(frame)
entry.grid(row=1, column=2,)
label2 = tkinter.Label(frame, text='Результат \n вычислений:')
label2.grid(row=2, column=0)
entry2 = tkinter.Entry(frame)
entry2.grid(row=2, column=2)
button = tkinter.Button(frame, text='Вычислить', command=v_sfery)
button.grid(row=3, column=1)
button1 = tkinter.Button(frame, text='Сохранить', command=save)
button1.grid(row=4, column=0)
tip = ttk.Combobox(frame, values=['Текст', 'HTML'])
tip.grid(row=4, column=2)
window.mainloop()
