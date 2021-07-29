# 모음은 몇 개나 있을까?

```python
def count_vowels(word):
	vowels = 'aeiou'
	total = 0
	for vowel invowels:
        total += word.count(vowel)
    
    return total 
```

# 정사각형만 만들기

```python
def only_square_area(a, b):
    lst = []
    for i in a:
        for j in b:
            if i == j:
                lst.append(i * j)
    return lst
            
print(only_square_area([32, 55, 63], [13, 32, 40, 55])) 
#=> [1024, 3025]
```

# 평균 점수 구하기

```python
def get_dict_avg(score_dict):
    total = 0
    count = 0
    for score in score_dict.values():
        total += score
        count += 1
    return total / count

---
# 내장함수 사용하면
	return sum(score_dict.values()) / len(score_dict)
```

# 혈액형 분류하기

```python
def count_blood(blood_info):
    blood_dict = {}
    for blood in blood_info:
        if blood_dict.get(blood): # 없을 시 None
            blood_dict[blood] += 1
        else:
            blood_dict[blood] = 1
    return blood_dict

---

def count_blood(blood_info):
    blood_dict[blood] = blood_dict.get(blood, 0) + 1 # 없을 시 0
```

# .extend()와 .append()

```python
list = [2, 4, 1, 3]

#list
list.append([8, 8]) # 리스트 마지막에 인자를 추가
list.extend([8, 8]) # 인자의 요소를 더해줌 (+와 같은 역할) 

print(list) #=> [2, 4, 1, 3, [8, 8], 8, 8]

#string
list.append('88') #=> ['88']
list.extend('88') #=> ['8','8']
```

# 무엇이 중복일까

```python
def duplicated_letters(word):
    result = []
    for char in word:
       # 1. 조건문으로 리스트에 중복되는 값이 들어가지 않게 하는 방법
       if word.count(char) > 1 and char not in result
           result.append(char)
    #return list(set(result)) # 2. set으로 리스트 중복 제거하는 방법
    return result

print(duplicated_letters('apple')) #=> ['p']
print(duplicated_letters('banana')) #=> ['a', 'n']
```

# 소대소대

```python
# for문 사용
def low_and_up(word):
    result = ""
    for idx in range(len(word)):
        if idx % 2: # odd
            result += word[idx].upper()
        else:
            result += word[idx].lower()
    return result

---

# 2. 리스트 컴프리헨션 + 조건 표현식 사용
result = [char.upper() if idx % 2 else char.lower() for idx, char in enumerate(word)] 
# (앞 if = 분류박스 표현식, 뒤 if = 필터) 
return ''.join(result)


print(low_and_up('apple')) #=> aPpLe
print(low_and_up('banana')) #=> bAnAnA
```

# 숫자의 의미

```python
def lonely(num_list):
    result = [num_list[0]] # 1. index 0의 값을 미리 넣는 방법
    for num in num_list:
    	if result[-1] != num:
            result.append(num)
	return result

---

# 2. enumerate 사용하여 index 접근하는 방법
def lonely(num_list):
    result = []
    for idx, num in enumerate(num_list)
    	if idx == 0:
            result.append(num)
        if result[-1] != num:
            result.append(num)
    return result

print(lonely([1, 1, 3, 3, 0, 1, 1])) #=> [1, 3, 0, 1] 
print(lonely([4, 4, 4, 3, 3])) #=> [4, 3] # 제거보다는 추가에 집중해보자
```

# Magic Method 

```python
__init__ : 생성자
__del__ : 소멸자
    
__str__ : 문자열 / print()할 때 보여지는 문자열 반환 / 외부 노출용
__repr__ : 문자열 / 인스턴스의 정보에 대한 값을 반환 (개발자가 개발할 때) / 내부용
    # 동작의 차이는 없음
```

# Basic Usages 

##### (https://github.com/joke2k/faker#basic-usage)

```python
1. faker 패키지에서 Faker # Pascal Case 클래스를 불러온다.
2. Faker는 클래스, fake는 인스턴스
3. name()은 fake의 인스턴스 메서드이다.
```

