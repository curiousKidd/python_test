# pip install requests beautifulsoup4

import requests
from bs4 import BeautifulSoup

# 오픈 api사용예정
# 기본 URL
url = "https://www.youthcenter.go.kr/opi/youthPlcyList.do"

# 쿼리 파라미터
params = {
    'openApiVlak' : '?????', #openapi key
    'display': '100',
    'pageIndex': '2',
    'srchPolyBizSecd': '003002001,003002004,003002008'
}

# GET 요청을 보내며 파라미터를 URL에 추가
response = requests.get(url, params=params)

# BeautifulSoup 객체를 생성합니다.
soup = BeautifulSoup(response.text, 'html.parser')


# 각 헤드라인의 텍스트를 출력합니다.
#for headline in headlines:
#   print(headline.text.strip())