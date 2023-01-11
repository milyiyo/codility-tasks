def solution(N):
    max_val = 0
    bin_repr = bin(N)[2:]

    is_counting = False
    temp_val = 0

    for n in bin_repr:
        if n == '1':
            max_val = max(max_val, temp_val)
            temp_val = 0
            is_counting = True

        if n == '0' and is_counting:
            temp_val += 1
    
    return max_val
