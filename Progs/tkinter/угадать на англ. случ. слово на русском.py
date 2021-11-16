import tkinter
import random
from tkinter import END

d = {'apple': 'яблоко', 'war': 'война', 'river': 'река', 'Earth': 'Земля', 'son': 'сын'}
n = 0


def rnd_rus():
    s = random.choice(list(d.values()))
    entry.delete(0, END)
    entry.insert(0, s)


def eng():
    global n
    i = str(entry2.get())
    if str(entry.get()) != d.get(i) and n == 0 or n == 1:
        entry3.delete(0, END)
        entry3.insert(0, 'Ошибка!')
        n += 1
    elif str(entry.get()) == d.get(i):
        entry3.delete(0, END)
        entry3.insert(0, 'Угадали!')
    elif n == 2:
        entry3.delete(0, END)
        entry3.insert(0, 'Последняя попытка!')
        n += 1
    else:
        window.destroy()


window = tkinter.Tk()
frame = tkinter.Frame().pack()
label = tkinter.Label(frame, text='Угадаешь это слово на английском? :)').pack()
entry = tkinter.Entry(frame)
entry.pack()
button1 = tkinter.Button(frame, text='Русское слово.', command=rnd_rus).pack()
entry2 = tkinter.Entry(frame)
entry2.pack()
button2 = tkinter.Button(frame, text='Сейчас проверим.', command=eng).pack()
label2 = tkinter.Label(frame, text='Результат:').pack()
entry3 = tkinter.Entry(frame)
entry3.pack()
window.mainloop()
