# 출석 체크

# 주어진 학생 n과 출석한 학생명부 students 문자열이 있다. 결석한 학생들로 구성된 문자열을 반환하시오.
# n이 7일 때, 1 2 3 4 5 6 7의 출석 번호가 부여되고,
# '1 3 5'는 출석한 학생 명부이다.
# 즉, 결석한 학생 명부 '2 4 6 7'을 return 해야 한다.

def check(n, students):
    lst = ""
    for i in range(1,n+1):
        if str(i) not in students:
            lst += str(i)
    return " ".join(lst)

print(check(7, '1 3 5')) #=> 2 4 6 7