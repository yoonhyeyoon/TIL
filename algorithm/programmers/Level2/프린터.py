def solution(priorities, location):
    answer = 0
    
    idx_lst = [c for c in range(len(priorities))]
    i = 0
    
    while True:
        
        if priorities[i] < max(priorities[i+1:]):
            priorities.append(priorities.pop(i))
            idx_lst.append(idx_lst.pop(i))
            
        else:
            i += 1
            
        if priorities == sorted(priorities, reverse=True):
            break
            
    answer = idx_lst.index(location) + 1
    return answer