import sys

def solve() :
    n = int(sys.stdin.readline())
    stairs = [0] * (n+1)
    for i in range(1, n+1) :
        stairs[i] = int(sys.stdin.readline())

    # n이 1이면 stairs[2]가 생기지 않게 되어 프로그램 터지는것 방지
    if n == 1 :
        print(stairs[1])
        return
    elif n == 2 :
        print(stairs[1] + stairs[2])
        return
    
    # dp에 층마다 저장할 수 있는 최대값을 모두 할당해 두고
    dp = [0] * (n+1)
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, n+1) :
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

    # 맨 위층만 출력
    print(dp[n])

solve()
