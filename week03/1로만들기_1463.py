import sys

num = int(sys.stdin.readline())

dp = [0] * (num+1)

for i in range(2, num+1) :
    dp[i] = dp[i-1] + 1
    if i%2 == 0 :
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i%3 == 0 :
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[num])

# 0 1 2 3 4 5 6 7 8 9 10

# 초기화
# 0 0 ...

# for문 시작
# 0 0 1
# 0 0 1 1               
# 0 0 1 1 2             
# 0 0 1 1 2 3
# 0 0 1 1 2 3 2
# 0 0 1 1 2 3 2 3                      
# 0 0 1 1 2 3 2 3 3
# 0 0 1 1 2 3 2 3 3 2
# 0 0 1 1 2 3 2 3 3 2 3