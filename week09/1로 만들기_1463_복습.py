import sys

def solve() :
    x = int(sys.stdin.readline())
    dp = [0] * (x+1) 

    for i in range(2, x +1) :  # 2일 때는 count가 1
        dp[i] = dp[i-1] + 1

        if i % 2 == 0 :
            dp[i] = min(dp[i], dp[i//2] + 1)

        if i % 3 == 0 :
            dp[i] = min(dp[i], dp[i//3] + 1)

    return(print(dp[x]))

solve()