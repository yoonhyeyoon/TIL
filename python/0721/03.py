# 리스트 중복 제거하기

def like_set(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    print(result)
        
like_set([1,2,3,4,1,2,3,4])


