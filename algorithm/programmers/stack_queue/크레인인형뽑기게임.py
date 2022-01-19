def solution(board, moves):
    answer = 0
    bucket = []
    
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1]:
                bucket.append(board[i][move-1])
                board[i][move-1] = 0
                if bucket[-1:] == bucket[-2:-1]:
                    answer += 2
                    bucket = bucket[:-2]
                break
    
    return answer