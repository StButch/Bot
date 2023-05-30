import requests #выгрузка сайта
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'}
directory = {'dollar_rub':
                 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D0%B0+'
                 '%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&oq=&aqs=chrome.0.35i39i362l6j69i59i450l2.59897062j0j7&sourceid='
                 'chrome&ie=UTF-8',
             'lari_rub':
                 'https://www.google.com/search?q=%D0%BA%D1%83%D1%80%D1%81+%D0%BB%D0%B0%D1%80%D0%B8+%D0%BA+%D1%80%D1%'
                 '83%D0%B1%D0%BB%D1%8E&newwindow=1&sxsrf=APwXEdc0w-Y9we_HaPW9AGrxj8PzzdjZgw%3A1684402264470&ei=WPBlZO'
                 'mjHLarxc8PiOKp6Aw&ved=0ahUKEwjpr4e1x_7-AhW2VfEDHQhxCs0Q4dUDCA8&uact=5&oq=%D0%BA%D1%83%D1%80%D1%81+'
                 '%D0%BB%D0%B0%D1%80%D0%B8+%D0%BA+%D1%80%D1%83%D0%B1%D0%BB%D1%8E&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIKCAAQg'
                 'AQQRhCCAjIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoKCAAQ'
                 'RxDWBBCwAzoKCAAQigUQsAMQQzoGCAAQBxAeOgcIIxCxAhAnOgcIABANEIAEOggIABAHEB4QCjoICAAQHhANEA86CggAEAUQHhA'
                 'NEA86CAgAEAgQHhANOg4IABCABBAKECoQRhCCAjoHCAAQgAQQCjoGCAAQFhAeSgQIQRgAUMQcWOBVYMtaaANwAXgBgAGaA4gBsxq'
                 'SAQowLjE0LjAuMi4xmAEAoAEByAEKwAEB&sclient=gws-wiz-serp'


             }



def get_currency(currency):
    try:
        return directory[currency]
    except Exception as e:
        return 'нет'


def get_exchange(currency):
    money = get_currency(currency)
    if money == 'нет':
        return 'Такой валюты нет'
    else:
        full_page = requests.get(money, headers=headers)
        soup = BeautifulSoup(full_page.content, 'html.parser')
        convert = soup.findAll('span',{'class':'DFlfde SwHCTb'})
        return(convert[0].text)


# def tracking(currency, difference):
#     target = float(get_exchange(currency).replace(',','.')) + difference
#     finish = datetime.now() + timedelta(hours = 6)
#     schedule.every(2).seconds.do(get_exchange, currency)
#
#     while datetime.now() < finish:
#         schedule.run_pending()
#
# tracking('dollar_rub',2)
#
# if z < target:
#     print(f'Курс изменился на {difference}\nБыло {track}, стало {get_exchange()}')
# else:
#     print('не достигеута')