import sys

def solve() :
    n = int(sys.stdin.readline())
    dp = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    
    # 아래에서 위로
    for i in range(n-2, -1, -1) : # 3 2 1 0
        for j in range(len(dp[i])) : # 4 3 2 1
            dp[i][j] += max(dp[i+1][j], dp[i+1][j+1]) 
            # 최초 실행시, 2층에서 1층 두 갈래 중 큰거 뽑아옴
        
    print(dp[0][0])

solve()
