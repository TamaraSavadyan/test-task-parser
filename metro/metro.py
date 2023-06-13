import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
import json

# URL = 'https://online.metro-cc.ru/'
URL = 'https://online.metro-cc.ru/category/bezalkogolnye-napitki/pityevaya-voda-kulery?from=under_search'
FILENAME = 'metro.csv'

headers = {
    'authority': 'api.metro-cc.ru',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'cookie': '_ym_uid=1685972128841561137; _ym_d=1685972128; _ga_YGMVQ8W6BY=GS1.1.1685972128.1.1.1685972249.9.0.0; _ga_97XSHVQ4WT=GS1.1.1685972128.1.1.1685972249.9.0.0; spid=1686497324692_cfc7f4cea961eb46d1f4ca6534285d95_let797tdcu0ux6lg; _slid=6485e85b76796bf8a10d3527; tmr_lvid=1ff1f8615e896876b6be147508810255; tmr_lvidTS=1686497475018; uxs_uid=04336a80-086d-11ee-b08e-a17f45c49870; fam_user=0 5; _slid_server=6485e85b76796bf8a10d3527; _ym_isad=1; allowedCookieCategories=necessary^%^7Cfunctional^%^7Cperformance^%^7Cpromotional^%^7CUncategorized; _gcl_au=1.1.802871831.1686594288; _gid=GA1.2.898672489.1686497477; local_ga=GA1.1.635304966.1686594291; local_ga_LV657197KB=GS1.1.1686594290.1.1.1686594748.60.0.0; ePNUserType=2; metro_user_id=2ac902feac1da1528fd151d3bcc66b58; _slfreq=633ff97b9a3f3b9e90027740^%^3A633ffa4c90db8d5cf00d7810^%^3A1686652613; XSRF-TOKEN=eyJpdiI6IlcyNlJ5T1FUQThVUVAzMk0wcVNZZ1E9PSIsInZhbHVlIjoiTW9DN1h5UlQ3NUczWHVNeGprb1wvMHd1NmtMbWkxbWduV0FxajdoN2VuNlRSQnNtaGRtejROTVphMnloeEZ4NngiLCJtYWMiOiJmMGZkMjQ4YjUxYzkwNTE4NzQ2ZWExOTc0YzBhMzEyZmQxZGE2MDE0ZmI5NzY1NzQ2NGQ2MmQ0NmMxZDMwM2NkIn0^%^3D; _slsession=885B7358-EBA6-423F-8638-205D44642905; metro_api_session=jDn3UlG6kGQY7RGpcWZZXUWx17A9fuGzB89XO6qH; _ym_visorc=b; _ga=GA1.2.393329437.1685972128; mindboxDeviceUUID=3e7ff6bd-8166-41cb-a8d3-a683126ce546; directCrm-session=^%^7B^%^22deviceGuid^%^22^%^3A^%^223e7ff6bd-8166-41cb-a8d3-a683126ce546^%^22^%^7D; _ga_VHKD93V3FV=GS1.1.1686649351.8.1.1686649460.0.0.0; at=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJwaG9uZSI6Ijc5MDk5MDE0OTY0IiwiY2FyZGhvbGRlcklkIjoiNzAwMDI3MDY5NjAxIiwidXBkYXRlU291cmNlIjoiZmFtaWx5UFJPRCIsInR5cGUiOiJhY2Nlc3MiLCJyZWZyZXNoVG9rZW5JZCI6Ijk2NzRjYmRlLTJiMzAtNDVhZS1hZmE0LTY1MzA1YWRiNDJmNCIsImlhdCI6MTY4NjY0OTQ2MywiZXhwIjoxNjg2NjUxMjYzLCJhdWQiOlsib3B2IiwibWFya2V0cGxhY2UiLCJtZXRyby1hdXRoLWFwcCJdLCJpc3MiOiJtZXRyby1hdXRoLWFwcCIsInN1YiI6Ijc5MDk5MDE0OTY0XzcwMDAyNzA2OTYwMSJ9.Atpt0sknFweWCtwb3TGe2HWze1TJuockVzfDiBFkXa04WrD2aPw2_An6hSboD3sNH0rJ9viEH8c2csGjgg0hjEHB6qLnvkBEruFuz_Ll5cvWxEIDZwa3E6P0Ea-QIP1uP4kmPxmxypYtWZq7Mt0glRkMbsKmZtI9lfMFmTpMj9o-0BZmvVtmSh12rnv_ckGU2XiCZcZeYeaOk425a4ioifzbKM2BbzAmBXRua9xVUg8jz-ui6jDpOI6ym_XtAQ-ts70B7iOQFbtFHv8FFseix2XLxbytnUgk-5tH11gQa-kooDqSlctBdBuTlVVTSM_Ox0rkZtQkOFCbfxsT7HIFSsPM7rwqZ0Ednsklqqm2VrLhOaK2V5Ha3FjcWHXl9OISrle355eaCwKroUKGseFCvucMSDbhvPJ3XX838VdkQeDXJR0Wn8Yeyrir8-9XXHOni5-ZA4HcjPKtWyXXG2pNZPzs-KQqw6Z_9_wQKdX69BRqUzFKgmMb52_6c69d3M7lW0YVG9Fr4GOX2l1Aert4U8Zc-_Bjz4MYGFrkWTcPEweBdG6Tm-06GPwKgYjvCcKhip3JccOXAoPc4fsFmShQXstUisEY7bxNHcWWjsTfCeQL50yFbkkO4RfA6uHpisOVAiVdXxwM1vZFXZre4EAwFfoVS_1fMPkbfSNfTVEBOtM; at_exp=1686651263000; rt=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6Ijk2NzRjYmRlLTJiMzAtNDVhZS1hZmE0LTY1MzA1YWRiNDJmNCIsInBob25lIjoiNzkwOTkwMTQ5NjQiLCJjYXJkaG9sZGVySWQiOiI3MDAwMjcwNjk2MDEiLCJ1cGRhdGVTb3VyY2UiOiJmYW1pbHlQUk9EIiwidHlwZSI6InJlZnJlc2giLCJpYXQiOjE2ODY2NDk0NjMsImV4cCI6MTcwMjIwMTQ2MywiYXVkIjpbXSwiaXNzIjoibWV0cm8tYXV0aC1hcHAiLCJzdWIiOiI3OTA5OTAxNDk2NF83MDAwMjcwNjk2MDEifQ.ixyYdG1AL1IbA6LYkjlUlM36qSsMXK2AzY5u8Vo2Ct6zXgMHCui-Uu4yE28N0HH73wHE_Ms64fKVEbcNX_1BXpGtCuguz2k8zievn2M5tZxf5CufU8Pu5frK20Zk0X-2Nv8ITCWTdv__D4wmFo-ZXtJ5o63eTKHi3yNXkYiSgGFttbrBpRPHBkEIurhXK3mKdL_l9wIRF8tJndsMEi7MpCYJstGM4Im_iY8lTolaP6K8pVXFGNwwOoaoy5xkxlbWlC2442kKfbhqr6J5VdbJpC7U1OGDvIlRBihNZ56VFIXNMkM815mZOLwyHxqYwsQ0UXaIDbDDd2ONkfNStzuIJY4nvHMhnGpueX-vxrZ4alj96NJ8aavFAKvBppeStPxiLUUYSyu1CvBFZp_lz82uBoy0K2I2l2LhhDnvekdvvyJhgLwm7du8OEngBHPXii45neGbJaPNm_GkqzujwFRlp2XBppMmb5zTFVrHgjdf5cAU-qpLO8xDg5a6hDlCK5796jW7A9sRju8Pob2GNC5yQjEbrn2ZTsO3ozPd9G3HG4OlXrDxpmJs6Im1JfSlG7FEyITkp7BTFF7yOyJW0O6b8ajbq5MnlDrksTPEjog0TLYojQ46v6pmHGisW9_LEof7eMimNH12eb7YgvWuj40oO-bPO-6a-o4IvnkGM2QnA; rt_exp=1702201463000; spsc=1686649464177_dd404108a2a4d5e4b0a1d7bb235c02e3_a5476469b72f558bb72e6aae99c6a060',
    'if-none-match': 'W/^\^"ee9f326ad368ff806204176606e78350^\^"',
    'origin': 'https://online.metro-cc.ru',
    'referer': 'https://online.metro-cc.ru/',
    'sec-ch-ua': '\^"Not.A/Brand^\^";v=^\^"8^\^", ^\^"Chromium^\^";v=^\^"114^\^", ^\^"Google Chrome^\^";v=^\^"114^\^"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '^\^"Windows^\^"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
}

def parse(url, headers):
    # код ниже не работает, просто скачала html с сайта и парсила его
    response = requests.get(url, headers=headers)
    soup = bs(response.text, 'lxml')
    print(response)

    # html с сайта, 'https://online.metro-cc.ru/category/bezalkogolnye-napitki/pityevaya-voda-kulery?from=under_search'
    with open('metro.html', 'rb') as file:
        source = file.read()

    soup1 = bs(source, 'lxml')    

    items = soup1.find_all('a', class_="product-card-name reset-link catalog-2-level-product-card__name style--catalog-2-level-product-card")
    with open('items.csv', 'w', encoding='utf-8') as file:
        for item in items:
            file.write(f'{str(item)}\n')


def get_data(json_file):

    result_to_csv = {
        'product_id': [], 
        'name': [], 
        'link': [],
        'regular_price': [],
        'promo_price': [],
        'brand': [],
        }
    
    result_to_json = []

    with open(json_file, 'r', encoding='utf-8') as file:
        json_ = json.load(file)

    for data in json_:
        result_to_csv['product_id'].append(data['ItemId'])
        result_to_csv['name'].append(data['Name'])
        result_to_csv['link'].append(data['Url'])
        result_to_csv['regular_price'].append(data['OldPrice'])
        result_to_csv['promo_price'].append(data['Price'])
        result_to_csv['brand'].append(data['Vendor'])

        result_to_json.append({
            'product_id': data['ItemId'], 
            'name': data['Name'], 
            'link': data['Url'],
            'regular_price': data['OldPrice'],
            'promo_price': data['Price'],
            'brand': data['Vendor'],
        })
   
    return result_to_csv, result_to_json


# parse(URL, headers)

with open('test.txt', 'r', encoding='utf-8') as file:
    src = file.decode('utf-8').read()

# with open('items.csv', 'r', encoding='utf-8') as file:
#     src = file.read()


print(src)




