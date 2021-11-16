import urllib.request
url = "http://dfedorov.spb.ru/python/files/tutchev.txt"
url1 = "http://dfedorov.spb.ru/python/files/tutchev.jpg"
# Все тэги для html взяты из страницы примера
with open("Тютчев.html", 'w', encoding='utf-8') as f:
    f.write("<html>"
            + "\n"
            + "<head>"
            + "\n"
            + "<meta charset='utf-8'>"
            + "\n"
            + "</head>"
            + "\n"
            + "<body>"
            + "\n")
    with urllib.request.urlopen(url) as web:
        t = 0
        for line in web:
            if t == 0:
                f.write("<p>"
                        + "\n"
                        + line.decode('utf-8')
                        + "\n"
                        + "</p>"
                        + "\n")
                t = t + 1
            else:
                f.write(line.decode('utf-8') + "<br>" + "\n")
    f.write("<p>"
            + "\n"
            + "<img src=" + url1 + ">"
            + "\n"
            + "</p>"
            + "\n"
            + "</body>"
            + "\n"
            + "</html>")
