import requests
import json

def send_kakao_message(data):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    headers = {
        "Authorization": "Bearer YOUR_ACCESS_TOKEN",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    message = "오늘의 청년 정책 정보:\n"
    for item in data['items']:
        message += f"- {item['polyBizSjnm']}:\n  {item['plcyTpNm']}\n  {item['rqutPrdCn']}\n\n"

    payload = {
        "template_object": json.dumps({
            "object_type": "text",
            "text": message,
            "link": {
                "web_url": "https://www.youthcenter.go.kr/"
            },
            "button_title": "청년센터 바로가기"
        })
    }

    response = requests.post(url, headers=headers, data=payload)

    if response.status_code == 200:
        print("메시지 전송 성공")
    else:
        print("메시지 전송 실패:", response.status_code, response.text)

# 예시 데이터로 메시지 전송
data = get_youth_policy_data()
if data:
    send_kakao_message(data)