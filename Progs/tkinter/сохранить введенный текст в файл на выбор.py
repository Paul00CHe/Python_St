import tkinter
from tkinter import ttk
from tkinter import END


def save():
    if str(tip.get()) == '.txt':
        with open('Написанный текст.txt', 'w') as s_f:
            for line in entry.get():
                s_f.write(line)
    elif str(tip.get()) == '.html':
        with open('Написанный текст.html', 'w') as s_f:
            for line in entry.get():
                s_f.write(line)
    else:
        entry.delete(0, END)
        entry.insert(0, 'Ошибка!')


window = tkinter.Tk()
frame = tkinter.Frame().pack()
label = tkinter.Label(frame, text='Напишите текст:').pack()
entry = tkinter.Entry(frame)
entry.pack()
label2 = tkinter.Label(frame, text='Выбирите расширение файла:').pack()
# выплывающий список
tip = ttk.Combobox(frame, values=['.txt', '.html'])
tip.pack()
button1 = tkinter.Button(frame, text='Сохранить в файл.', command=save).pack()
window.mainloop()
