import sys

def solve() :
    n = int(sys.stdin.readline())
    
    if n <= 2 :
        print(1)
        return

    dp = [0] * (n+1)
    dp[1] = 1 # 첫 숫자는 1로 고정
    dp[2] = 1 # n을 2로 받을때도 10 만 가능

    # 추가 첨부한 사진과 같이 결과값이 피보나치 수열 공식과 동일
    for i in range(3, n+1) :
        dp[i] = dp[i-1] + dp[i-2]

    print(dp[n])

solve()
    
