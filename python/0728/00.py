# 2차원 리스트의 숫자 합 반환하기
numbers = [
    [1, 4],
    [10, 5],
    [20, 30]    
]

# 1. for 문 활용하여 풀이
def sum_list(numbers):
    total = 0
    for number in numbers:
        for num in number:
            total += num
    return total

print(sum_list([[1, 4], [10, 5], [20, 30]])) #=> 70

# 2-1. Index로 접근하여 풀이
def sum_list_index(numbers):
    total = 0
    for idx in range(len(numbers)):
        total += sum(numbers[idx])
    return total
# 2-2 
def sum_list_index(numbers):
    total = 0
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            total += numbers[i][j]
    return total

# 3. While 문 활용하여 풀이
def sum_list_while(numbers):
    i = 0
    total = 0
    while i < len(numbers):
        j = 0
        while j < len(numbers[i]):
            total += numbers[i][j]
            j += 1
        i += 1
    return total
