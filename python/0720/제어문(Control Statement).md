# 제어문(Control Statement)

:pushpin: ​[파이썬 문서](https://docs.python.org/ko/3/tutorial/controlflow.html)

> 순서도(Flow Chart)

![61180553-25e87b00-a653-11e9-9895-7976d7204734](제어문(Control Statement).assets/61180553-25e87b00-a653-11e9-9895-7976d7204734.png)

## 조건문(Conditional Statement)

`if` 문은 반드시 **참/거짓을 판단할 수 있는 조건**과 함께 사용이 되어야 한다.

* if 조건문의 구성

```python
if <expression>:
    <코드 블럭>
elif <expression>:
    <코드 블럭>
else:
    <코드 블럭>
```

* 조건 표현식(Conditional Expression) == 삼항 연산자(Ternary Operator)

  ```python
  true_value if <조건식> else false_value
  ```

  

## 반복문(Loop Statement)

### 1. While 문

`while` 문은 조건식이 참(`True`)인 경우 반복적으로 코드를 실행한다.

* while 문의 구성

```python
while <조건식>:
    <코드 블럭>
```

* **4spaces**로 들여쓰기
* 반드시 종료조건을 설정해야 한다.

### 2. For 문

`for` 문은 시퀀스(string, tuple, list, range)를 포함한 순회가능한 객체(iterable)의 요소들을 순회한다.

* for 문의 구성

```python
for <임시변수> in <순회가능한데이터(iterable)>:
    <코드 블럭>
```

* `for` 문에서 요소 값에 다른 값을 할당해도 다음 반복구문에 영향을 주지 않는다.

```python
for i in range(10):
    print(i)
    i = 5 # 영향을 주지 않는다.
```

* `enumerate()`

  * [내장 함수](https://docs.python.org/ko/3.6/library/functions.html) 중 하나이며, 다음과 같이 구성되어 있다.

  > ![61180561-3993e180-a653-11e9-9558-085c9a0ad65d](제어문(Control Statement).assets/61180561-3993e180-a653-11e9-9558-085c9a0ad65d.png)

  ```python
  lunch = ['짜장면', '초밥', '피자']
  for idx, menu in enumerate(lunch):
      print(idx, menu) 
  # 0 짜장면
  # 1 초밥
  # 2 피자
  ```

* 반복제어

  * `break`

    * 반복문을 종료
    * `for` 나 `while` 문에서 빠져나간다.

  * `continue`

    * `continue` 이후의 코드를 수행하지 않고, 다음 요소부터 계속하여 반복한다.

  * `for-else`

    * `break` 시행 안 되면 `else` 시행 된다.

    * `break `시행 되면 `else` 시행 안 된다.

    ```python
    for i in range(3):
        print(i)
        if i == 1:
            print(f'{i}에서 break 시행됨.') # <- 시행O
            break
    else:
        print('break 시행안됨.') # <- 시행X
    ```

  * `pass`

