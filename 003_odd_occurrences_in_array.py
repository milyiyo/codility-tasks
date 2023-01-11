def solution(A):
    count_info = {}
    
    for x in A:
        if x in count_info:
            count_info[x] += 1
        else:
            count_info[x] = 1

    for k,v in count_info.items():
        if v % 2 == 1:
            return k 

    return 0
