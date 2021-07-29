# oop

# 2인 1조 클래스 만들기

# 초기화 메서드는 인자로 학생 이름으로 구성된 리스트를 받아서 인스턴스 변수에 할당한다.
# pick(n) 메서드는 학생들 명단에서 인자 n명 만큼 랜덤으로 추출하여 return한다.
# match_pair() 메서드는 학생들 명단을 랜덤으로 2명씩 매칭해 준다. 이때, 학생들 명단의 수가 홀수명이면 단 한팀만 3명으로 구성한다.

import random 

class ClassHelper:
    def __init__(self, student):
        self.student = student
    
    def pick(self, n):
        result = random.sample(self.student, n)
        return result
    
    def match_pair(self):
        random.shuffle(self.student)
        pair_cnt = len(self.student) // 2
        pairs = []
        for cnt in range(pair_cnt):
            if cnt == pair_cnt - 1: # 마지막 조는 2명이거나 3명
                pair = self.student[cnt*2:] # 끝까지 슬라이싱 
                pairs.append(pair)
                break
            pair = self.student[cnt*2:cnt*2+2]
            pairs.append(pair)
        return pairs

ch = ClassHelper(['김코딩', '이코딩', '조코딩', '박코딩', '정코딩'])

print(ch.pick(1)) #=> ['이코딩']
print(ch.pick(1)) #=> ['김코딩']
print(ch.pick(2)) #=> ['김코딩', '박코딩']
print(ch.pick(3)) #=> ['김코딩', '조코딩', '정코딩']
print(ch.pick(4)) #=> ['박코딩', '이코딩', '김코딩', '정코딩']

ch.match_pair() #=> [['조코딩', '이코딩'], ['김코딩', '정코딩', '박코딩']]