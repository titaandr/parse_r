import requests
from bs4 import BeautifulSoup
import re

HOST = 'https://www.avito.ru/'
URL = 'https://www.avito.ru/moskva/avtomobili/infiniti/q50?cd=1&radius=0'
HEADERS = {\
    'user-agent': \
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko)'
        ' Chrome/78.0.3904.108 Safari/537.36',\
        'accept' : '*/*' \
}

def get_html(url,params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r

def get_content(html):
    soup = BeautifulSoup(html.text, 'html.parser')
    #items = soup.find_all('h3', class_= 'snippet-title')
    items = soup.find_all('div', class_= 'description item_table-description')
    #print(items)

    cars = []
    for item in items:
        try:
            cars.append({
                'title': item.find('a', class_='snippet-link').get('title'),
                'links': HOST + item.find('a', class_='snippet-link').get('href'),
                'price': item.find('span', class_='price').contents[0]

            })
        except AttributeError:
            print('err')
    print(cars)





def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html)
    else:
        print('error')
#    print(html.status_code)


parse()