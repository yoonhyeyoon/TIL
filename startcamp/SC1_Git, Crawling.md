# Git



### 절대경로 / 상대경로

* command - cd : 폴더이동 , date : 현재 시간 , ls : 현재 파일 목록 보기, 

* touch : 파일생성 , mkdir : 폴더생성

* (+) ~ : home 

  



### git

* git : 사진첩! 분산버전관리시스템

* github, gitlab, bidbuscket : 제공 서비스 

* git init -> git 관리 시작

* git commit -m 'log'

* cd .. , ls

  



### git 순서

* ~~git init~~
* git add .
* git status (상태확인)
* git cummit -m '*log*'
* git push origin master

git commit -m 'add files'



# Crawling

```python
import requests
from bs4 import BeautifulSoup 

# 네이버 국내증시 크롤링 (비공식 경로)
response = requests.get('https://finance.naver.com/marketindex/').text
html = BeautifulSoup(response, 'html.parser')

print(html.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text)

#KOSPI_now
```









