def min_jumps(int_list):
    N = len(int_list)
    infinity = float("inf")
    
    if N == 0 or int_list[0] == 0:
        return infinity
    
    jumps = [infinity] * N
    jumps[0] = 0
    
    for i in range(1, N):
        for j in range(i):
            if j + int_list[j] >= i:
                jumps[i] = min(jumps[i], jumps[j] + 1)
                
    
    if jumps[N-1] == infinity:
        return infinity
    
    return jumps[N-1]


test = [2,2,2,3,4,1,1,2,3,1,1]

a=min_jumps(test)
print(a)


