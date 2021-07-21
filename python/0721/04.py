# 특정 숫자 포함 여부 출력하기 (is 안 쓰기)

def find_number(lst, num):
    t_or_f = 0
    for i in lst:
        if i == num:
            print(f"{num} => True")
            t_or_f = 1
            break

    if t_or_f == 0:
        print(f"{num} => False")

find_number([2,4,6],3)