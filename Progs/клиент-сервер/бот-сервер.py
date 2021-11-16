import socket
import random
HOST = '127.0.0.1'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
while True:
    # 1 - количество подключений в очереди (1-один подключающийся)
    s.listen(1)
    conn, addr = s.accept()
    print('Connected client', addr)
    data = conn.recv(1024).decode('utf-8')
    if not data:
        break
    elif data == 'Проверка':
        data2 = 'Привет! Я могу рассказать тебе анекдоты на темы: еды, животных, школы! Выбирай!:)'
    elif data == 'животных':
        A = []
        with open('Анекдоты про животных.txt', 'r', encoding='utf-8') as f:
            B = f.readlines()
            B1 = []
            for i in B:
                if i.strip() != '==':
                    B1.append(i.strip())
                    continue
                else:
                    A.append(''.join(B1))
                B1.clear()
            data2 = random.choice(A[1:])
    elif data == 'школу':
        A = []
        with open('Анекдоты про школу.txt', 'r', encoding='utf-8') as f:
            B = f.readlines()
            B1 = []
            for i in B:
                if i.strip() != '==':
                    B1.append(i.strip())
                    continue
                else:
                    A.append(''.join(B1))
                B1.clear()
            data2 = random.choice(A[1:])
    elif data == 'еду':
        A = []
        with open('Анекдоты про еду.txt', 'r', encoding='utf-8') as f:
            B = f.readlines()
            B1 = []
            for i in B:
                if i.strip() != '==':
                    B1.append(i.strip())
                    continue
                else:
                    A.append(''.join(B1))
                B1.clear()
            data2 = random.choice(A[1:])
    conn.send(data2.encode('utf-8'))
    print('Send: ', data2)
conn.close()

