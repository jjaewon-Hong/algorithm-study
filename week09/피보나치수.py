import sys

# 1 1 2 3 5 8 13
def solve() :
    n = int(sys.stdin.readline())
    dp = [1] * (n+1)

    for i in range(3, n+1) :
        dp[i] = dp[i-1] + dp[i-2]

    return(print(dp[n]))

solve()
