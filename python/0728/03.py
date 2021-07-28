# 주어진 문자열(text)에서 제시된 알파벳(alphabet)의 등장 위치를 리스트로 반환하시오. 해당 알파벳이 등장하지 않으면, -1을 반환하시오.


def my_find(text, alphabet):
    lst = []
    for i in range(len(text)): # for idx, char in enumerate(text)
        if text[i] == alphabet:
            lst += [i]
    if not lst:
        return -1
    return lst

print(my_find('apple', 'p')) #=> [1, 2]
print(my_find('a', 'p')) #=> -1 