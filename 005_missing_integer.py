def solution(A):
    if max(A) < 0:
        return 1
    
    filtered = set(A)
    hash_table = {}
    for x in filtered:
        hash_table[x] = None
    
    val = 1
    while True:
        if val in hash_table:
            val += 1
        else:
            return val

    return val
