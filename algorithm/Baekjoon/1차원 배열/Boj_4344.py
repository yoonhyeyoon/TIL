# 평균넘는 학생 비율 구하기

n = int(input())

for i in range(n):
    scores = list(map(int, input().split()))
    average = sum(scores[1:]) / scores[0]
    cnt = 0
    result = 0
    for score in scores[1:]:
        if average < score:
            cnt += 1
    result = cnt / scores[0] * 100
    print(f"{result:.3f}%")