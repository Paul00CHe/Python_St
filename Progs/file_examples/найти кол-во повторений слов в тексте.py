import urllib.request
url = "http://dfedorov.spb.ru/python3/src/romeo.txt"
L = ""
A = []
with urllib.request.urlopen(url) as web:
    for line in web:
        L = line.strip().decode("utf-8").replace(',', '').replace('.', '').split()
        # print(L, type(L))
        A.extend(L)
# print(A, A.count("is"))
# Для слова по запросу
# chastota = dict()
# for i in A:
    # chastota[i] = A.count(i)
# y = input("Введите слово: ")
# print("В отрывке это слово встречается, раз: ", chastota[y])


def hist(S):
    d = dict()
    for c in S:
        if c not in d:
            d[c] = 1
        else:
            d[c] = d[c] + 1
    return d


print(hist(A))
