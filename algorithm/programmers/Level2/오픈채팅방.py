def solution(record):
    answer = []
    dic = {}
    for rec in record:
        lst = rec.split()
        if len(lst) == 3:
            dic[lst[1]] = rec.split()[2]
    for rec in record:
        lst = rec.split()
        if lst[0] == "Enter":
            answer.append(f"{dic[lst[1]]}님이 들어왔습니다.")
        elif lst[0] == "Leave":
            answer.append(f"{dic[lst[1]]}님이 나갔습니다.")
    return answer