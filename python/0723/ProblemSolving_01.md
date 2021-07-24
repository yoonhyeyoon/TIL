# Mutable & Immutable

```python
mutable = List, Set, Dictionary
immutable = String, Tuple, Range
```

# 홀수만 담기

```python
lst = []
for i in range(1, 51):
    if i % 2:
        lst.append(i) 
print(lst)

---

lst = list(range(1, 51))
odd = lst[::2]
```

# 반복문으로 네모 출력

```python
for i in range(1, m+1):
    print('*' * n) 

---

for i in range(m):
    for j in range(n):
        print('*', end="")
    print(" ")   
```

# 조건 표현식

```python
temp = 36.5
print('입실 불가') if temp >= 37.5 else print('입실가능')
```

# 평균 구하기

```python
scores = [80, 89, 99, 83]
sum = 0
for i in scores:
    sum += i
print(sum / len(scores))
```

# 간단한 N의 약수

```python
num = int(input())

for i in range(1, num+1):
    if num % i == 0:
        print(i, end=" ")
```

# 중간값 찾기

```python
numbers = [
    85, 72, 38, 80, 69, 65, 68, 96, 22, 49, 67,
    51, 61, 63, 87, 66, 24, 80, 83, 71, 60, 64,
    52, 90, 60, 49, 31, 23, 99, 94, 11, 25, 24
]

numbers.sort() # sorted(numbers)
mid = 0

for i in range(1, len(numbers)+1):
    if len(numbers) % 2:
        mid = numbers[len(numbers) // 2]
print(mid)

---

length = 0
for num in numbers:
    length += 1
    
center = length // 2
sort_list = sorted(numbers)
print(sort_list[center])
```

# 계단 만들기

```python
number = int(input())

step = ""

for i in range(1, number+1):
    step += str(i) + " "  
    print(step)
    
---

for i in range(number):
    for j in range(1, i+2):
        print(f'{j}, end='')
    print('')
```

# Built-in 함수

```python
print(), abs(), list(), dict(), tuple() 
```

# 정중앙 문자

```python
def get_middle_char(char):
    if len(char) % 2:
        print(char[len(char)//2])       
    else:
        print(char[len(char)//2-1],char[len(char)//2]) 
        
---

def get_middle_char(char): 
	idx = len(char) // 2
    if len(char) % 2:
        return char[idx]
    else:
        return char[idx-1:idx+1]
```

# 가변 인자 리스트

```python
def my_avg(*num):
    cnt = 0
    total = 0
    for i in num:
        cnt += 1
        total += i
    return(total / cnt)
```

# List의 합 구하기

```python
def list_sum(lst):
    total = 0
    for i in lst:
        total += i

    return total
```

# Dictionary로 이루어진 List의 합 구하기

```python
def dict_list_sum(lst):
    total = 0
    for i in lst:
        for key, value in i.items():
            if key == 'age':
                total += value 
    return total

---

	for i in lst:
        total += i['age']
    return total
```

# 2차원 List의 전체 합 구하기

```python
def all_list_sum(lst):
    total = 0
    for i in lst:
        for j in i:
            total += j
    return total 
```

# 아스키코드 변환하기

```python
def get_secret_word(n):
    list = ""
    for i in n:
       list += chr(i) # chr, ord
    return list
```

```python
def get_secret_number(n):
    total = 0
    for i in n:
        total += ord(i)
    return total

get_secret_number('tom') #=> 336
```

# 절댓값 구하기

```python
def my_abs(x):
    if type(x) == complex:
        return (x.real**2 + x.imag**2) ** 0.5
    else:
        if x == 0:
            return x ** 2
        elif x < 0:
            return -x
        else:
            return x
```

# `all()` 직접 구현하기

```python
def my_all(elements):
    for i in elements:
        if not i:
            return False
        
    return True
```

# `any()` 직접 구현하기

```python
def my_any(elements):
    for i in elements:
        if i:
            return True
        
    return False
```

