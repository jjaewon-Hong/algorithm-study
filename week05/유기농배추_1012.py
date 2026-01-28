# M 가로길이(세로줄개수), N 세로길이(가로줄개수),  K 배추 심어진 위치의 개수 
# 접근 방식 -> 플러드 필
# 1) 배추위치 1로 다 받음
# 2) 1인 애들 주변 돌면서 0으로 바꿈
# 3) 더 이상 주변에 1이 없으면 재귀 사용하여 다음 1로 넘어감 
import sys
sys.setrecursionlimit(10000) # 재귀 깊이 제한 늘려줌

num = int(sys.stdin.readline())
graph = []

def dfs(x,y) :
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    graph[y][x] = 0

    for i in range(4) :
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < M and 0 <= ny < N : 
            if graph[ny][nx] == 1: # 덩어리 내의 1을 모조리 찾아냄
                dfs(nx, ny)

T = int (sys.stdin.readline())

for _ in range(T) :
    M, N, K = list(map(int, sys.stdin.readline().split()))
    graph = [[0] * M for _ in range(N)]
    for _ in range(K) :
        x, y = list(map(int, sys.stdin.readline().split()))
        graph[y][x] = 1

    count = 0

    for i in range(N) :
        for j in range(M) :
            if graph[i][j] == 1:  # 최초의 1 덩어리를 찾기 위한 조건문
                dfs(j, i)
                count += 1

    print(count)
                
