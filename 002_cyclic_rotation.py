def solution(A, K):
    if len(A) == 0:
        return A
   
    tmp = [x for x in A]
    
    for i in range(K):
        tmp.insert(0, tmp[-1])
        tmp = tmp[:-1]

    return tmp
