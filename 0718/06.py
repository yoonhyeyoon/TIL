# 단어 회문 판단하기 

def back_word():
    word = input("단어를 입력하세요: ")
    back_word = ""
    for i in word:
        back_word = i + back_word
    print(back_word)
    if word == back_word:
        print("입력하신 단어는 회문(Palindrome)입니다.")

back_word()