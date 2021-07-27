# 데이터 구조(Data Structure) II

> - 알고리즘에 빈번히 활용되는 순서가 없는(unordered) 데이터 구조
>   - 세트(Set)
>   - 딕셔너리(Dictionary)

## 세트(Set)

> 변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)

#### 1. 추가 및 삭제

* `.add(elem)`
  * elem을 세트에 추가
* `.update(*others)`
  * 여러 값 추가
  * 인자로 반드시 iterable 데이터 구조 전달
* `.remove(elem)`
  * elem을 세트에서 삭제
  * 없으면 KeyError 발생
* `.discard(elem)`
  * elem을 세트에서 삭제
  * 없어도 에러 발생하지 않음
* `.pop()`
  * 임의의 원소(랜덤)를 제거해 반환

## 딕셔너리(Dictionary)

> 변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)
>
> `Key: Value` 페어(pair)의 자료구조

#### 1. 조회

* `.get(key[, default])`
  * key를 통해 value를 가져옴
  * 절대 KeyError 발생하지 않음
  * default는 None

#### 2. 추가 및 삭제

* `.pop(key[, default])`
  * 제거하고 그 값을 반환
  * key가 딕셔너리에 없으면 default 반환
  * default가 없는 상태에서 딕셔너리에 없으면 KeyError 발생
* `.update()`
  * 값을 제공하는 key, value로 덮어씀

#### 3. 딕셔너리 순회

* dictionary에서 `for`를 활용하는 4가지 방법

```python
# 0. dictionary 순회 (key 활용)
for key in dict:
    print(key)
    print(dict[key])


# 1. `.keys()` 활용
for key in dict.keys():
    print(key)
    print(dict[key])


# 2. `.values()` 활용
# 이 경우 key는 출력할 수 없음
for val in dict.values():
    print(val)


# 3. `.items()` 활용
for key, val in dict.items():
    print(key, val)
```

> 딕셔너리 구축하기

```python
book_title =  ['great', 'expectations', 'the', 'adventures', 'of', 'sherlock', 'holmes', 'the', 'great', 'gasby', 'hamlet', 'adventures', 'of', 'huckleberry', 'fin']

# 1. dict[key] 접근
word_count = {}
for title in book_title:
    if title in word_count:
        word_count[title] += 1
    else:
        word_count[title] = 1

# 2. count 메서드 활용
word_count = {}
for title in book_title:
	word_count[title] = book_title.count(title)
        
# 3. get 메서드 활용
word_count = {}
for title in book_title:
    word_count[title] = word_count.get(title, 0) + 1
```

#### 4. Dictionary comprehension

* 표현 구조

```python
{키: 값 for 요소 in iterable}

dict({키: 값 for 요소 in iterable})
```

* 활용

> 세제곱 딕셔너리

```python
cubic = {i: i**3 for i in range(1, 9)}
#=> {1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216, 7: 343, 8: 512}
```

> negative_blood_types

```python
blood_types = {'A': 40, 'B': 11, 'AB': 4, 'O': 45}

blood_types = {f'-{key}': value for key, value in blood_types.items()}
#=> {'-A': 40, '-B': 11, '-AB': 4, '-O': 45}
```

> Dictionary comprehension + 조건

```python
{키: 값 for 요소 in iterable if 조건식}
```

