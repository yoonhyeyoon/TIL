# 가위바위보 게임하기 

def rock_paper_scissors_game(a, b):
    win_rule = {'가위':'보', '바위':'가위', '보':'바위'}
    if a ==  b:
        print("비겼습니다!")
    else: 
        if win_rule[a] == b:
            print(f"{a}가 이겼습니다!")
        else:
            print(f"{b}가 이겼습니다!")

gamer1 = input("홍길동씨는 무엇을 내겠습니까? ")
gamer2 = input("이순신씨는 무엇을 내겠습니까? ")

rock_paper_scissors_game(gamer1, gamer2)

