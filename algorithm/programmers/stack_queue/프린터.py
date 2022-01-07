def solution(priorities, location):
    answer = 0
    loc = 0
    cnt = 0
    while priorities:
        j = priorities.pop(0)
        
        for prioritie in priorities:
            if j < prioritie:
                priorities.append(j)
                cnt += 1
            
            
        loc += 1
        if loc == location:
            answer = cnt-len(priorities)+1
    
    return answer