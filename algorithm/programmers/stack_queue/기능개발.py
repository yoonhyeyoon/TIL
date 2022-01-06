# 입출력 순서? -> 스택 큐 

def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    
    while progresses:
        if progresses[0] + (speeds[0]*time) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count:
                answer.append(count)
                count = 0
            time += 1
    
    answer.append(count)
    
    return answer