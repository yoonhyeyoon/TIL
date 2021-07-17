* command
  * `cd ..` : 폴더이동  
  * `date` : 현재 시간 
  * `ls` : 현재 파일 목록 
  * `touch` : 파일생성 
  * `mkdir` : 폴더생성



# Git

> Git은 분산버전관리시스템(DVCS : Distributed Version Control System) 이다.
>
> 소스코드의 버전 및 이력을 관리할 수 있다.



** Github, Gitlab, Bidbuscket은 이를 제공하는 서비스이다.*

---



## Ready to Git

git bash 설치 후, `author` 정보를 생성해준다.

````
git config --global user.name {user name}
git config --global user.email {user email}
````



## Git 순서

#### 1. 저장소 생성

```bash
$ git init 
```

`.git` 폴더가 생성된다.



#### 2. add

```bash
$ git add file.py # 특정 파일
$ git add . # 모든 파일
```

`working directory` 에서 작업한 사항을 `staging area` 에 올린다.

`add .` 이 편하지만, 올리지 않아야 할 파일을 주의한다.



#### 3. status

```bash
$ git status 
```

`staging area`에 파일이 잘 올라와 있는 지 상태를 확인한다.



#### 4. commit

```bash
$ git commit -m 'first commit' 
```

`local history`로 커밋한다.

* 반드시 `log` 메시지에 변경사항을 명확하게 입력해주어야한다.
* 해당 시점을 스냅샷으로 만들어 기록한다.



 #### 5. push

```bash
$ git push origin master # (or main)
```

`repository` 원격저장소로 업로드한다.





# Crawling

> 네이버 국내증시 크롤링 (비공식 경로)

```python
import requests
from bs4 import BeautifulSoup 

response = requests.get('https://finance.naver.com/marketindex/').text
html = BeautifulSoup(response, 'html.parser')

print(html.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text)

#KOSPI_now
```









