def solution(participant, completion):
    answer = ''
    hash_table = {}

    for p in participant:
        if hash_table.get(p):
            hash_table[p] += 1
        else:
            hash_table[p] = 1

    for c in completion:
        hash_table[c] -= 1

    for key, value in hash_table.items():
        if value > 0:
            answer = key

    return answer