# 합격 메시지 출력하기

# 풀이 1 

student_score = {1:88, 2:30, 3:61, 4:55, 5:95}
for student, score in student_score.items():
    if score >= 60:
        print(f"{student}번 학생은 {score}점으로 합격입니다.")
    else:
        print(f"{student}번 학생은 {score}점으로 불합격입니다.")

# 풀이 2
student_score = [88, 30, 61, 55, 95]
for i in range(0,5):
    if student_score[i] >= 60:
        ispass = '합격'
    else:
        ispass = '불합격'
    print(f"{i+1}번 학생은 {student_score[i]}점으로 {ispass}입니다.")
