import requests
from bs4 import BeautifulSoup

URL = 'http://www.metacritic.com/game/playstation-4'

def cli():
    items = fetch_list()

    for elem in items:
        print(elem['score'], elem['title'])


def fetch_list():
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36'

    }
    res = requests.get(URL, headers=headers)

    # NOTE: maybe treat 2xx as success?
    if res.status_code == 200:
        return parse_html(res.content)

    return []


def parse_html(content):
    # NOTE: This is brittle and WILL break in the future (tm)
    soup = BeautifulSoup(content, 'html5lib')
    listing = soup.find('ol', class_='list_products list_product_summaries')
    products = listing.find_all('div', class_='wrap product_wrap')

    items = []
    for item in products:
        # TODO: Some exception handling is in order here (e.g. None has no
        # .get_text())
        title = item.find('h3', class_='product_title').get_text()
        score = int(item.find('a', class_='basic_stat product_score').get_text())

        items.append({'title': title, 'score': score})

    return items
