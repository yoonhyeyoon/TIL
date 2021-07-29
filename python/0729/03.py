# 데이터구조

# 중복되지 않은 숫자의 합

# 같은 숫자가 한개 있거나 두개가 들어있는 리스트가 주어진다. 
# 이러한 리스트에서 숫자가 한개만 있는 요소들의 합을 구하는 함수 sum_of_repeat_number()를 작성하시오.

# 1
def sum_of_repeat_number(numbers):
    total = 0
    for number in numbers:
        if numbers.count(number) == 1:
            total += number
    return total

# 2. 변수사용
def sum_of_repeat_number(numbers):
    once = []
    multiple = []
    for number in numbers:
        if number in once: # 이미 once에 있으면 multiple로 옮긴다.
            multiple.append(number)
            once.remove(number)
        elif number not in multiple:  # 처음 등장
            once.append(number) # once에 추가
    return sum(once)

sum_of_repeat_number([4, 4, 7, 8, 10, 4]) # => 25
            