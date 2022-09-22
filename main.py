from bs4 import BeautifulSoup
import requests
from data import KEYWORDS, headers, main_url, url


res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res, features='html.parser')

news_articles = soup.find_all("article")
for news_article in news_articles:
    previews = news_article.find("div", class_="tm-article-snippet")
    previews = [preview.text.split() for preview in previews]
    for i in previews:
        for b in KEYWORDS:
            if b in i:
                day_pok = news_article.find("span", class_="tm-article-snippet__datetime-published").text
                title_pok = news_article.find("a", class_="tm-article-snippet__title-link").text
                url_pok = news_article.find("a", class_="tm-article-snippet__title-link").get("href")
                print(f"{day_pok} ==> {title_pok} ==> {main_url+url_pok}")
