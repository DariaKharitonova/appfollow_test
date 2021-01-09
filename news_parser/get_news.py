import requests
from bs4 import BeautifulSoup
from news_parser.news import add_news

URL = 'https://news.ycombinator.com/'


def get_news():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, features="lxml")
    news = soup.find_all('tr', class_='athing')
    return news


def insert_to_db():
    result = []
    news = get_news()
    for item in news:
        post_id = item.get('id')
        post_info = item.find('a', class_='storylink')
        title = post_info.get_text()
        link = post_info.get('href')
        add_news(title, link, post_id)
        result.append({
            'post_id': post_id,
            'title': title,
            'link': link
        })
    print('result')
    return result
