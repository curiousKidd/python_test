# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# 네이버 뉴스 페이지에서 HTML을 가져옵니다.
response = requests.get("https://news.naver.com/")

# BeautifulSoup 객체를 생성합니다.
soup = BeautifulSoup(response.text, 'html.parser')

# 뉴스 헤드라인을 선택합니다.
headlines = soup.select("div.sch-result-wrap div.result-list-wrap._item_contents div.cjs_news_tw div.cjs_t")

# 각 헤드라인의 텍스트를 출력합니다.
for headline in headlines:
    print(headline.text.strip())