import sys

def solve() :
    n = int(sys.stdin.readline())
    dp = [1] * (n+1)

    for i in range(2,n+1) :
        dp[i] = (dp[i-1] + dp[i-2]) % 10007
        
    return(print(dp[n]))

solve()
        