# 회문 판별하기

def is_pal_while(word):
    while len(word) > 1:
        if word[0] == word[-1]:
            word = word[1:-1]
        else:
            return False
    return True

# (재귀함수 이용)
def is_pal_recursive(word):
    if len(word) <= 1:
        return True
    if word[0] == word[-1]:
        return is_pal_recursive(word[1:-1])
    else:
        return False