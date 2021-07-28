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

# 학생별 총합 (sum()이용하지 않기)
# 1. 인덱스 이용 (더 좋은 접근)
for i in range(len(students)):
    score = 0 
    for j in range(len(students[i])):
        score += students[i][j]
    print(score) 
    #=> 280
      # 240
      # 240

# 2. for문 이용 (단순한 방법)
for student in students:
    total = 0
    for score in student:
        total += score
    print(total)
