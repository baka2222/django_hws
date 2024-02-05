from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup
import requests


'''Если что парсинг домом в Бишкеке'''


URL = 'https://www.house.kg/kupit-dom'
HEADERS = {
    'Accept': 'image/avif,image/webp,image/apng,image/svg+xml,image/*,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}


@csrf_exempt
def get_html(url, params=''):
    html = requests.get(url, headers=HEADERS, params=params)
    return html


@csrf_exempt
def get_data(html):
    bs = BeautifulSoup(html, 'html.parser')
    items = bs.find_all('div', class_='listing')
    items_list = []
    for i in items:
        items_list.append(
            {
                'title': i.find('p', class_='title').get_text().strip(),
                'price': i.find('div', class_='price').get_text(),
                'location': i.find('div', class_='address').get_text().strip(),
                'img': str(i.find('img', class_='temp-auto').attrs['data-src']) #Писал то, что у find'а нету get()
            }                                                                 #Поэтому сделал через attrs
        )                                                                      #конкатенация вроде не нужна
    return items_list


#Здесь я не прописал декоратор, так как при запуске принта этой функции, он запрашивал параметр request
#Не зная, как его достать, я решил не прописывать декоратор, но парсер работает
def parser():
    html = get_html(URL)
    if html.status_code == 200:
        houses_info = []
        for page in range(1):
            html = get_html(URL, params={'page': page})
            houses_info.extend(get_data(html.text))
        return houses_info
    else:
        raise Exception('Переделай код!')

# print(parser())





