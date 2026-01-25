import sys

n = int(sys.stdin.readline())
sum = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(1, n) :
    for j in range(len(sum[i])) :
        if j == 0 :
            sum[i][j] += sum[i-1][j]
        elif j == len(sum[i]) - 1 :
            sum[i][j] += sum[i-1][j-1]
        else :
            sum[i][j] += max(sum[i-1][j-1], sum[i-1][j])

print(max(sum[n-1]))
# 맨 밑에 수부터 담으면 값을 증가해보는 형태
# 위에서 부터 밑으로 가면 작은값 골랐다가 큰 값 고르는 경우가
# 항상 큰값 고르는것 보다 최종적으로 더 큰 값이 되는 예외 상황을 완전히 배제시킴