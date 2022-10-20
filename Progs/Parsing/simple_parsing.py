import requests
from bs4 import BeautifulSoup

url = 'https://quotes.toscrape.com/' # сайт
response = requests.get(url) # получаем разметку сайта
soup = BeautifulSoup(response.text, 'lxml') # записываем в переменную разметку в формате .lxml
quotes = soup.find_all('span', class_='text') # выбираем цытаты из разметки по тегу span
authors = soup.find_all('small', class_='author') # выбираем авторов из разметки по тегу small
tags = soup.find_all('div', class_='tags') # выбираем все теги по тегу div, класс tags

for i in range(0, len(quotes)):
    print(quotes[i].text) # вывод текста цитаты
    print('--' + authors[i].text) # вывод автора цитаты
    tagsforquote = tags[i].find_all('a', class_='tag') # вывод тегов
    for tagforquote in tagsforquote:
        print(tagforquote.text)
    print('\n')