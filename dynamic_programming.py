def thribDP(n):
    memo = {}
    return thribMem(n,memo)

def thribMem(n,memo):
    if n <= 2:
        memo[n] = 2-n
    
    if n in memo:
        return memo[n]
    else:
        memo[n] = (3 * thribMem(n-1,memo)) + (2* thribMem(n-2,memo)) + (thribMem(n-3,memo))  
    return memo[n]


def thribDPBU(n):
    memo = {}

    memo[0] = 2
    memo[1] = 1
    memo[2] = 2

    if n in memo:
        return memo[n]
    else:
        for i in range(3,n+1):
            memo[i] =  (3*memo[i-1]) + (2*memo[i-2]) + (memo[i-3])
    return memo[n]