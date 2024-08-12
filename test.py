import requests

def get_youth_policy_data():
    url = "https://www.youthcenter.go.kr/opi/youthPlcyList.do"
    params = {
        'openApiVlak': 'your_api_key',  # API 키를 여기에 입력하세요
        'pageIndex': 1,
        'display': 10,  # 한 페이지에 표시할 결과 수
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("API 요청 실패:", response.status_code)
        return None

data = get_youth_policy_data()
print(data)