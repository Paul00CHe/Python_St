import tkinter
from tkinter import END


def convert():
    # entry передает строку, поэтому преобразуем в число
    fahrenheit = int(entry.get())
    # для вывода в поле обратно преобразуем в строку
    s = str((fahrenheit - 32) * 5 / 9)
    # очищаем поле вывода
    entry2.delete(0, END)
    # выводим в поле
    entry2.insert(0, s)


def ex():
    window.destroy()


window = tkinter.Tk()
# либо во фрейме, либо в самом окне будут поля
frame = tkinter.Frame()
frame.pack()
# поле (label - метка(обозначение полей)) с названием поля, что будет ниже
label = tkinter.Label(frame, text='Temperature in Fahrenheit:')
label.pack()
# поле для ввода данных в переменную entry
entry = tkinter.Entry(frame)
entry.pack()
# поле куда будет выведен результат
entry2 = tkinter.Entry(frame)
entry2.pack()
# кнопка пересчета
button1 = tkinter.Button(frame, text='Convert', command=convert)
button1.pack()
# кнопка выхода
button2 = tkinter.Button(frame, text='Quit', command=ex)
button2.pack()
window.mainloop()
