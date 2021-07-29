#  썩은 과일 찾기

# 과수원에 농부 한명이 썩은 과일이 몇개 들어있는 과일 봉지를 가지고 있다. (과일 봉지는 리스트를 의미한다.)
# 썩은 과일 조각들을 모두 신선한 것으로 교체하는 함수 change_rotten_fruit()를 작성하시오.

# 데이터 구조

# 만약 리스트가 null/nil/None이거나 비어 있는 경우 빈 리스트를 반환한다.
# 반환된 리스트의 요소는 모두 소문자여야 한다.

# 1
def change_rotten_fruit(fruit_bag):
    new_bag = []
    for fruit in fruit_bag:        
        if 'rotten' in fruit:
            fruit = fruit.lstrip('rotten') 
            fruit = fruit.lower()
            new_bag.append(fruit)
            continue
        new_bag.append(fruit)
    return new_bag

# 2. if 안 하고
def remove_rotten(fruit_bag):
    result = []
    for fruit in fruit_bag:
        fruit = fruit.replace('rotten', '') # 활용
        fruit = fruit.lower()
        result.append(fruit)
    return result

change_rotten_fruit(['apple', 'rottenBanana', 'apple']) 
#=> ['apple', 'banana', 'apple']

change_rotten_fruit(['rottenapple', 'rottenBanana', 'apple', 'rottenGrape']) 
#=> ['apple', 'banana', 'apple', 'grape']