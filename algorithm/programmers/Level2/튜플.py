def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key = len)
    for ss in s:
        sss = ss.split(',')
        for ssss in sss:
            if int(ssss) not in answer:
                answer.append(int(ssss))
    return answer