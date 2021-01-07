import json
import csv
import requests
from bs4 import BeautifulSoup

URL = 'https://tvset.tut.by/category/10/'
HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0', 'accept': '*/*'}
	              
HOST = 'https://tvset.tut.by'
OUT_FILENAME = 'tv.json'
TELEGRAM_TOKEN = ''
CHAT_ID = ''
FILE = 'tv.csv'


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('article', class_='channel')
    tv_programm = []   
    for item in items:
        tv_programm.append({
            'title': item.find('h2', class_='channel-name').get_text(strip=True),
            'link':  item.find('ul', class_='channel-programm').get_text().replace('\n', ' '),
        })
        with open(OUT_FILENAME, 'w', encoding="utf-8") as f:
            json.dump(tv_programm, f, ensure_ascii=False, indent=1)

    # Чтобы увидеть результат удалить хэш из print
    #print(tv_programm)
    return tv_programm

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

with open('tv.json', 'r', encoding="utf-8") as f:
    s = json.load(f)
    title = s[41]['title']
    link = s[41]['link']

def knopki():
    title = s[41]['title']
    link = s[41]['link']

knopki()

title = s[41]['title']
link = s[41]['link']