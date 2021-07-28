# 2차원 리스트의 항목 별 합 반환하기

# A반 학생들의 점수는 아래와 같고, students 리스트에 저장되어 있다.
# A학생(국어 100점, 수학 80점, 영어 100점)
# B학생(국어 90점, 수학 90점, 영어 60점)
# C학생(국어 80점, 수학 80점, 영어 80점)

students = [
 [100, 80, 100],
 [90, 90, 60],
 [80, 80, 80]
]

# 과목별 총합 (sum()이용하지 않기)
for i in range(len(students)):
    total = 0
    for j in range((len(students[i]))):
        total += students[j][i]
    print(total)

# 지그재그 순회
l = [
  [1, 2, 3],
  [4, 5, 6], 
  [7, 8, 9]
]
print('행 우선')
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[i][j], end=' ')
    print()
print('열 우선')
for i in range(len(l)):
    for j in range(len(l[i])):
        print(l[j][i], end=' ')
    print()

# 행 우선
# 1 2 3 
# 4 5 6 
# 7 8 9 
# 열 우선
# 1 4 7 
# 2 5 8 
# 3 6 9 