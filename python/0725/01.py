# 자릿수 더하기

def sum_of_digit(number):
    total = 0
    for i in str(number):
        total += int(i)
    return total

# OR

def sum_of_digit(number):
    total_sum = 0
    while number:
        remainder = number % 10
        number = number // 10
        total_sum += remainder
    return total_sum

print(sum_of_digit(1234))



# (재귀함수 이용)
def sum_of_digit(number):
    if number < 10:
        return number
    else:
        number, remainder = divmod(number, 10)
        return sum_of_digit(number) + remainder