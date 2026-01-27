# [참고 메모]
# 파이썬의 깊이 제한 1000
# 정수 오버플로우를 신경쓰지 않아도 될 만큼 유연하게 처리

import sys

N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N) :
    graph.append(list(map(int, sys.stdin.readline().strip())))

dx = [-1,1,0,0] # 좌우
dy = [0,0,-1,1] # 상하

queue = [[0,0]]

while queue :
    x, y = queue.pop(0) 
    # 최초 queue.pop(0) 동작시 [0,0]이 x에 0, y는 0으로 각각 담김  

    for i in range(4) : # [-1,0] -> [1,0] -> [0,-1] -> [0,1] (상 -> 하 -> 좌 -> 우)
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= N or ny < 0 or ny >= M : # 테두리 벗어나면 무시
           continue

        if graph[nx][ny] == 0: # 벽 무시 
            continue

        if graph[nx][ny] == 1:
            graph[nx][ny] = graph[x][y] + 1 # 이전 좌표에서 +1 받는 형태
            queue.append([nx, ny])

print(graph[N-1][M-1])