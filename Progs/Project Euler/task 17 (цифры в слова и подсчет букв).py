# Если записать числа от 1 до 5 английскими словами (one, two, three, four, five),
# то используется всего 3 + 3 + 5 + 4 + 4 = 19 букв.
# Сколько букв понадобится для записи всех чисел от 1 до 1000 (one thousand) включительно?
# Примечание: Не считайте пробелы и дефисы. Например, число 342 (three hundred and forty-two) состоит из 23 букв,
# число 115 (one hundred and fifteen) - из 20 букв. Использование "and" при записи чисел соответствует правилам
# британского английского.
EngChisl = dict()
EngChisl[1] = 'one'
EngChisl[2] = 'two'
EngChisl[3] = 'three'
EngChisl[4] = 'four'
EngChisl[5] = 'five'
EngChisl[6] = 'six'
EngChisl[7] = 'seven'
EngChisl[8] = 'eight'
EngChisl[9] = 'nine'
EngChisl[10] = 'ten'
EngChisl[11] = 'eleven'
EngChisl[12] = 'twelve'
EngChisl[14] = 'fourteen'
EngChisl['13-30'] = 'thir'
EngChisl['13-19_ok'] = 'teen'
EngChisl[15] = 'fif'
EngChisl[20] = 'twen'
EngChisl[40] = 'for'
EngChisl[80] = 'eigh'
EngChisl['20-90_ok'] = 'ty'
EngChisl[100] = 'hundred'
EngChisl[1000] = 'thousand'


def NamToWord(x):
    if x < 100:
        if x <= 14 and x != 13:
            x = EngChisl[x]
        elif x == 13:
            x = EngChisl['13-30'] + EngChisl['13-19_ok']
        elif x == 15:
            x = EngChisl[x] + EngChisl['13-19_ok']
        elif 16 <= x <= 19 and x != 13:
            x = list(str(x))
            x = EngChisl[int(x[1])] + EngChisl['13-19_ok']
        elif x == 20 or x == 40:
            x = EngChisl[x] + EngChisl['20-90_ok']
        elif x == 30:
            x = EngChisl['13-30'] + EngChisl['20-90_ok']
        elif x == 50:
            x = EngChisl[15] + EngChisl['20-90_ok']
        elif x == 80:
            x = EngChisl[80] + EngChisl['20-90_ok']
        elif x == 60 or x == 70 or x == 90:
            x = list(str(x))
            x = EngChisl[int(x[0])] + EngChisl['20-90_ok']
        elif 21 <= x <= 29:
            x = list(str(x))
            x = EngChisl[20] + EngChisl['20-90_ok'] + '-' + EngChisl[int(x[1])]
        elif 41 <= x <= 49:
            x = list(str(x))
            x = EngChisl[40] + EngChisl['20-90_ok'] + '-' + EngChisl[int(x[1])]
        elif 31 <= x <= 39:
            x = list(str(x))
            x = EngChisl['13-30'] + EngChisl['20-90_ok'] + '-' + EngChisl[int(x[1])]
        elif 51 <= x <= 59:
            x = list(str(x))
            x = EngChisl[15] + EngChisl['20-90_ok'] + '-' + EngChisl[int(x[1])]
        elif 81 <= x <= 89:
            x = list(str(x))
            x = EngChisl[80] + EngChisl['20-90_ok'] + '-' + EngChisl[int(x[1])]
        elif 61 <= x <= 79 or 91 <= x <= 99 and x != 60 and x != 70 and x != 80 and x != 90:
            x = list(str(x))
            x = EngChisl[int(x[0])] + EngChisl['20-90_ok'] + '-' + EngChisl[int(x[1])]
    elif x == 100 or x == 200 or x == 300 or x == 400 or x == 500 or x == 600 or x == 700 or x == 800 or x == 900:
        x = list(str(x))
        x = EngChisl[int(x[0])] + ' ' + EngChisl[100]
    elif 101 <= x <= 999 and x != 100 and x != 200 and x != 300 and x != 400 and x != 500 \
            and x != 600 and x != 700 and x != 800 and x != 900:
        x = list(str(x))
        x = EngChisl[int(x[0])] + ' ' + EngChisl[100] + ' and ' + NamToWord(int(x[1] + x[2]))
    elif x == 1000:
        x = list(str(x))
        x = EngChisl[int(x[0])] + EngChisl[1000]
    return x


S = []
for i in range(1, 1001):
    a = list(NamToWord(i).replace('-', '').replace(' ', ''))
    S.append(len(a))
print(sum(S))
