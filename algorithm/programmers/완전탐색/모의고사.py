def solution(answers):
    answer = []
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 1, 2, 3, 2, 4, 2, 5]
    l3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0,0,0]
    
    for i in range(len(answers)):
        if l1[i%5] == answers[i]:
            score[0] += 1
        if l2[i%8] == answers[i]:
            score[1] += 1
        if l3[i%10] == answers[i]:
            score[2] += 1
            
    for i, s in enumerate(score):
        if s == max(score):
            answer.append(i+1)
    
    return answer