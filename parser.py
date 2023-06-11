import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


URL = 'https://online.metro-cc.ru/'
FILENAME = 'output.csv'

def parse(url):
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    print(response)

    result = {
        'product_id': [], 
        'name': [], 
        'link': [],
        'regular_price': [],
        'promo_price': [],
        'brand': [],
        }

    items = soup.find_all('div', class_='product-title')

    for item in items:
        product_id = item['data-product-id']
        name = item.find('div', class_='product-title').text.strip()
        link = item.find('a', class_='product-name')['href']
        regular_price = item.find('span', class_='regular-price').text.strip()
        promo_price = item.find('span', class_='promo-price').text.strip()
        brand = item.find('div', class_='brand').text.strip()

        result['product_id'].append(product_id)
        result['name'].append(name)
        result['link'].append(link)
        result['regular_price'].append(regular_price)
        result['promo_price'].append(promo_price)
        result['brand'].append(brand)

    return result


products = parse(URL)

df = pd.DataFrame(products)
df.to_csv(FILENAME, index=False)

