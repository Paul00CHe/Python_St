import urllib.request
import re
url = "http://dfedorov.spb.ru/python/files/mbox-short.txt"
with open("Список строк с почтой.txt", 'w') as f:
    with urllib.request.urlopen(url) as web:
        for i in web:
            i = i.decode('utf-8')
            if re.search("[@]", i) != None:
                f.write(i)
            else:
                continue
