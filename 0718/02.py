# pop함수 이용해서 80점 이상의 점수들의 총합 구하기

score = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
total = 0

while len(score):
    i = score.pop()
    if i >= 80:
         total += i 

print(total)