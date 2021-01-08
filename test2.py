import json
import csv
import requests
from bs4 import BeautifulSoup

URL = 'https://programma-peredach.com'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0', 'accept': '*/*'}

OUT_FILENAME = 'tv.json'

FILE = 'tv.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_='channel')
    tv_programm = []   
    for item in items:
        tv_programm.append({
            'title': item.find('div', class_='title').get_text(strip=True),
            'link':  item.find('div', class_='line2 proListShort').get_text().replace('\t', '').replace('\n', ' '),
        })
        #Запись в JSON формат:
        with open(OUT_FILENAME, 'w', encoding="utf-8") as f:
            json.dump(tv_programm, f, ensure_ascii=False, indent=1)

    # Чтобы увидеть результат удалить хэш из print
    #print(tv_programm)
    return tv_programm

#Запись в CSV формат:
def save_file(items, path):
    with open(path, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['Марка', 'Ссылка'])
        for item in items:
            writer.writerow([item['title'], item['link']])
            #print(item['link'])

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        tv_programm = get_content(html.text)
        save_file(tv_programm, FILE)
    else:
        print('Error')

parse()