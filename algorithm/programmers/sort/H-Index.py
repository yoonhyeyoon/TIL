def solution(citations):
    answer = 0
    l = len(citations)
    h = 0
    
    while h <= l: 
        cnt = 0
        for citation in citations:
            if citation >= h:
                cnt += 1
        if cnt >= h:
            answer = h
        h += 1
    return answer