import tkinter
from tkinter import ttk
from tkinter import END
import socket
HOST = '127.0.0.1'
PORT = 50007


# Получили ответ, что делает бот
def enter():
    # каждый раз надо создавать объект типа сокет
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    ping = 'Проверка'
    s.send(ping.encode('utf-8'))
    data = s.recv(1024).decode('utf-8')
    entry.delete(0, END)
    entry.insert(0, data)
    s.close()


# Получили анекдот по выбранной теме
def get():
    # каждый раз надо создавать объект типа сокет
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    A = str(tip.get())
    if A == 'животных' or A == 'школу' or A == 'еду':
        s.send(A.encode('utf-8'))
        data4 = s.recv(1024).decode('utf-8')
        entry.delete(0, END)
        entry.insert(0, data4)
        s.close()
    else:
        entry.delete(0, END)
        entry.insert(0, 'Выберите тему для анекдота!')


window = tkinter.Tk()
window.geometry('300x200')
frame = tkinter.Frame().pack()
label = tkinter.Label(frame, text='Расказчик анекдотов').pack()
button = tkinter.Button(frame, text='Нажми меня!', command=enter)
button.pack()
button1 = tkinter.Button(frame, text='Расскажи мне анекдот про:', command=get)
button1.pack()
tip = ttk.Combobox(frame, values=['животных', 'школу', 'еду'])
tip.pack()
entry = tkinter.Entry(frame, width=40)
entry.pack()
window.mainloop()
