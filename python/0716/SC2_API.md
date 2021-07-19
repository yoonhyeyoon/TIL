# API

> 약자로, Application Programming Interface 애플리케이션 프로그래밍 인터페이스이다.
>
> * 운영체제 (window, mac, ios, android ...) 가 서버(응용프로그램)에 **요청**했을 때 **응답**을 보여주는 플랫폼이다.
>
> * 서버와 서버간의 대화  

```python
# 1.정보가 있는 API URL을 확인한다.
url = 'https://" 

# 2. URL로 요청을 보낸다.
response = requests.get(url).json() 

# 3. 응답 결과를 확인하고 정보를 찾는다.
print(response)
```

* `json()` ->`json`으로 표현된 코드를 `list`나 `dictionary`로 보여준다.





## Example

>  공공데이터 API

```python
import requests

# 미세먼지
Key = "" # 숨김
durl = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?sidoName=서울&stationName=강남구&serviceKey={Key}&returnType=json'
response = requests.get(durl).json()
dust = response["response"]["body"]["items"][0]["pm10Value"]
msg = f"서울의 미세먼지 농도는 {dust}입니다."

#텔레그렘
TOKEN = "" # 숨김
turl = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=1868177818&text={msg}"
response = requests.get(turl).json

```



> naver sopping API

```python
import requests
from pprint import pprint # 예쁘게 프린트

# 네이버 API
query = '닌텐도스위치' 
url = f"https://openapi.naver.com/v1/search/shop.json?query={query}"

head = {
    'X-Naver-Client-Id' : '', # hide
    'X-Naver-Client-Secret' : '' # hide
}

response = requests.get(url, headers=head).json()


# 1. 반복문 사용하여 각 제품마다 lprice를 출력하기

items = response['items']
min_value = 9999999
title = ''
min_url = ''

for i in items:
    #pprint= i['lprice']

# 2. 최저가를 찾아서 최저가를 출력하기
    if min_value > int(i['lprice']):
        min_value = int(i['lprice'])

        # 3. 최저가명, 최저가, 최저가 쇼핑몰 링크
        title = i['title']
        min_url = i['link']

print(f'{title} \n 최저가 : {min_value} \n 링크 : {min_url}')



# 4. 텔레그램으로 출력

# 텔레그렘
TOKEN = " " # hide
msg = f'{title} \n 최저가 : {min_value} \n 링크 : {min_url}'
turl = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id=1868177818&text={msg}"
response = requests.get(turl).json
```

