def solution(genres, plays):
    answer = []
    hash_map = {}
    
    for i in range(0, len(genres)):
        if genres[i] in hash_map:
            hash_map[genres[i]].append((plays[i], i))
        else:
            hash_map[genres[i]] = [(plays[i], i)]
    
    while hash_map:
        for genre in hash_map.keys():
            hash_map[genre].sort(key=lambda x:-x[0])
            total = 0
            max_num = 0
            max_genre = ''
            for play in hash_map[genre]:
                total += play[0]
                if max_num < total:
                    max_num = total
                    max_genre = genre

        for i in range(0, 2):
            answer.append(hash_map[max_genre][i][1])
        hash_map.pop(max_genre)

    return answer