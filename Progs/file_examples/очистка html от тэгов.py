import urllib.request
url = "http://dfedorov.spb.ru/python/files/p.html"
L = ""
with urllib.request.urlopen(url) as web:
    for line in web:
        line = line.decode('utf-8')
        L = L + line
    t = 0
    S = ""
    for i in range(len(L)):
        if L[i] == "<":
            t += 1
            continue
        elif L[i] == ">":
            t = 0
            continue
        elif L[i] != "<" and L[i] != ">" and t == 1:
            continue
        else:
            S = S + L[i]
print(S.replace('  ', ' ').strip())
