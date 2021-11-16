L = "Мой дядя самых честных правил, Когда не в шутку занемог, Он уважать себя заставил И лучше выдумать не мог"
g = L.split()
b = []
for i in g:
    if i.startswith("м") or i.startswith("М"):
        continue
    else:
        b.append(i)
s = ' '.join(b)
print(s)
