# 한수

def hansu(number):
    hansu = 0
    for num in range(1, number+1):
        if num < 100:
            hansu += 1
        else:
            num = list(map(int, str(num))) # str으로 형변환하여 list에 하나씩 넣고 int로 다시 형변환
            if num[1] - num[0] == num[2] - num[1]:
                hansu += 1
    print(hansu)