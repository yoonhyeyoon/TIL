# 데이터 구조(Data Structure) I

> **Program = Data Structure + Algorithm**
>
> \- Niklaus Wirth -
>
> - 알고리즘에 빈번히 활용되는 순서가 있는(ordered) 데이터 구조
>   - 문자열(String)
>   - 리스트(List)
> - 데이터 구조에 적용 가능한 Built-in Function

## 문자열(String)

> 변경할 수 없고(immutable), 순서가 있고(ordered), 순회 가능한(iterable)

:pushpin:  [조작법 (method)](https://docs.python.org/ko/3/library/stdtypes.html#string-methods)

#### 1. 조회/탐색

* `.find(x)`
  * x의 **첫 번째 위치**를 반환
  * 없으면, `-1`을 반환
* `.index(x)`
  * x의 **첫 번째 위치**를 반환
  * 없으면, 오류 발생

#### 2. 문자열 변경

* `.replace(old, new[, count])`
  * 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
  * count 지정 시 해당 갯수만큼만 시행

* `.strip([chars])`
  * 양쪽 제거 (strip)
  * 왼쪽 제거 (lstrip)
  * 오른쪽 제거 (rstrip)
  * 문자 지정 안할 시, 공백 제거

* `.stlit([chars])`

  * 특정한 단위로 나누어 리스트로 반환

* `'separator'.join(iterable)`

  * 특정한 문자열로 만들어 반환
  * 반복가능한(iterable) 컨테이너의 요소들을 separator(구분자)로 합쳐(`join()`) 문자열로 반환

  ```python
  word = '배고파'
  words = ['안녕', 'hello']
  
  '!'.join(word) #=>'배!고!파'
  ' '.join(words) #=>'안녕 hello'
  ```

* `.capitalize()`, `.title()`, `.upper()`

  * `.capitalize()` : 앞글자를 대문자로 만들어 반환
  * `.title()` : 어포스트로피나 공백 이후를 대문자로 만들어 반환
  * `.upper()` : 모두 대문자로 만들어 반환

* `.lower()`, `.swapcase()`

  * `lower()` : 모두 소문자로 만들어 반환
  * `.swapcase()` : 대 <-> 소문자로 변경하여 반환

* ```python
  .isalpha(), .isdecimal(), .isdigit(), .isnumeric(), .isspace(), .isupper(), .istitle(), .islower() # 문자열 관련 검증 
  ```

```
+-------------+-----------+-------------+----------------------------------+
| isdecimal() | isdigit() | isnumeric() |          Example                 |
+-------------+-----------+-------------+----------------------------------+
|    True     |    True   |    True     | "038", "੦੩੮", "０３８"             |
|  False      |    True   |    True     | "⁰³⁸", "🄀⒊⒏", "⓪③⑧"          |
|  False      |  False    |    True     | "↉⅛⅘", "ⅠⅢⅧ", "⑩⑬㊿", "壹貳參"   |
|  False      |  False    |  False      | "abc", "38.0", "-38"             |
+-------------+-----------+-------------+----------------------------------+
```

```python
# dir 함수로 문자열이 가지고 있는 메소드를 확인할 수 있다.
dir('')
```

## 리스트(List)

> 변경 가능하고(mutable), 순서가 있고(ordered), 순회 가능한(iterable)

#### 1. 값 추가 및 삭제

* `.append(x)`
  * 리스트에 값을 추가
* `.extend(iterable)`
  * 리스트에  iterable(list, range, tuple, string**[주의]**) 값을 붙일 수가 있다.
  * list concatenate와 동일 (+)
* `.insert(i, x)`
  * 정해진 인덱스 `i`에 값을 추가

* `.remove(x)` 
  * 리스트에서 값이 x인 것을 삭제
* `.pop(i)`
  * 정해진 위치 `i`에 있는 값을 삭제하며, 그 항목을 반환
  * `i`가 지정되지 않을 시, 마지막 항목 삭제, 반환
* `.clear()`
  * 리스트의 모든 항목을 삭제

#### 2. 탐색 및 정렬

* `.index(x)`
  * x 값을 찾아 해당 index 값을 반환
* `.count(x)`
  * 원하는 값을 개수를 반환
* `.sort()`
  * 정렬
  * 내장함수 `sorted()` 와는 다르게 **원본 list를 변형**시키고, `None`을 리턴

* `.reverse()`
  * 반대로 뒤집는다. (정렬아님)

#### 3. 리스트 복사

> 변경가능한(`mutable`) 데이터
>
> * `list`
> * `dict`
> * `set`

#### 3-1. 얕은 복사(shallow copy)

* slice 연산자 사용 `[:]`

```python
a = [1, 2, 3]
b = a[:] 

b[0] = 5
print(a) #=> [1, 2, 3] 원본 값이 변경되지 않음 
```

* `list()` 활용

```python
b = list(a)
```

* `copy` 모듈 활용

```python
import copy

b = copy.copy(a)
```

#### 3-2. 깊은 복사(deep copy)

* `copy` 모듈 활용

```python
import copy

a = [1, 2, [1, 2]] # 중첩된 상황
b = copy.deepcopy(a)
```

#### 4. List Comprehension

> 표현식과 제어문을 통해 리스트를 생성
>
> 여러 줄의 코드를 한 줄로 줄인다.

* 표현 구조

```python
[expression for 변수 in iterable]

list(expression for 변수 in iterable)
```

* 활용 

> 세제곱 리스트

```python
# 반복문
cube_list = []
for i in numbers:
    cube_list.append(i**3)
print(cube_list)

# List Comprehension 활용
cubic_list = [i**3 for i in numbers]
```

> List Comprehension + 조건

```python
[expression for 변수 in iterable if 조건식]
```



## 데이터 구조에 적용가능한 Built-in Function

> iterable 타입 - `list`, `dict`, `set`, `str`, `bytes`, `tuple`, `range` 

* `map(function, iterable)`

  * iterable의 모든 요소에 function 적용, 반환
  * return은 `map_object`형태
  * 입력값을 처리할 때 자주 활용

  ```python
  # case1
  new_numbers = map(int, input('두 정수를 입력하세요.').split())
  # case2
  numbers = ['1', '2', '3']
  new_numbers = list(map(int, numbers)) #=> [1, 2, 3]
  # case3
  # 세제곱 함수 map 활용
  def cube(n):
      return n ** 3
  new_numbers = list(map(cube, numbers))
  ```

* `filter(function, iterable)`

  * iterable에서 funtion의 반환된 결과가 `True`인 것들만 구성해서 반환
  * `filter object`를 반환

  ```python
  # 홀수판별 함수 filter 활용
  def odd(n):
      return n % 2
  
  numbers = [1, 2, 3]
  new_numbers = list(filter(odd, numbers))
  ```

* `zip(*iterables)`

  * 복수의 iterable 객체를 모아 (`zip()`) 해준다.
  * **튜플**의 모음으로 구성된 `zip object` 반환

  ```python
  girls = ['jane', 'ashley', 'mary']
  boys = ['justin', 'eric', 'david']
  
  # zip() 활용하여 짝을 맞추어 본다.
  pair = list(zip(girls, boys)) #=> [('jane', 'justin'), ('ashley', 'eric'), ('mary', 'david')]
  
  # .join 과 zip 활용하여 full_name 함수 생성
  def full_name(*args):
      name_list = [' '.join(name) for name in zip(*args)]
      return name_list
  
  result = full_name(last_name, first_name) #=> ['jane justin', 'ashley eric', 'mary david']
  
  # 전치 행렬 
  a = [
      [1, 1, 1],
      [2, 2, 2],
      [3, 3, 3]
  ]
  
  b = list(zip(*a)) #=> [(1, 2, 3), (1, 2, 3), (1, 2, 3)]
  
  # 딕셔너리에 넣기
  key_list = ['key1', 'key2', 'key3']
  value_list = ['justin', 'eric', 'david']
  
  easy_dict = dict(zip(key_list, value_list)) #=> {'key1': 'justin', 'key2': 'eric', 'key3': 'david'}
  ```

  