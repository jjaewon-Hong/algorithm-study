# 근처 부터 찾는 bfs 특성 활용 해야함
# 어차피 익은것에서 4방향으로 다 익어지기 때문에 
# 여기서 말하는 최소는 상자의 모든 부분이 1 or 더 이상 하루가 지나도 변화가 없는 상태를 의미
import sys
from collections import deque 
# (미로 찾기는 리스트로만 풀어서 deque 활용)

M, N = map(int, sys.stdin.readline().split())
# M=가로칸, N=세로칸수(=한줄 수)

graph = []
queue = deque() # 좌표 담을 큐 생성 () 

for i in range(N) :
    row = list(map(int, sys.stdin.readline().split())) # 한줄 전체를 리스트 형태로 저장
    graph.append(row) # [ [row1] [row2] ...]
    for j in range(M) :
        if row[j] == 1 :
            queue.append((i, j)) # [ (x,y) , (x1,y2) ... ]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 배열에 1만 채우는 방식이 아니라 익는 날짜별로 숫자 채워 나가는 방식
while queue :
    x, y = queue.popleft() 

    for i in range(4) : # '상하좌우' 순으로 탐색
        nx = x + dx[i]
        ny = y + dy[i] 

        if 0 <= nx < N and 0 <= ny < M : # 테두리 안벗어나고
            if graph[nx][ny] == 0: #0인 상태면
                graph[nx][ny] = graph[x][y] + 1 # 카운트
                # 1로 다 채워보는게 아니라 한 칸 이동할 때 마다 n+1 형태로 채워나감

                queue.append((nx, ny)) # 다음 위치만 저장 
                # queue.popleft()의 동작 수 != 카운트 수
                # ex)   2  
                #     2 1 2
                #       2    이런 형태면 동작수는 4번이지만 최종(최대) 카운트는 2로 책정됨

max_days = 0

# 일단 위에 queue 반복문으로 그래프를 전부 세팅은 한상태 
#  -> 이제 노드 하나씩 검사하며 최댓값 구하자
for row in graph:
    for cell in row:
        if cell == 0:        # 하나라도 안 익은(0) 게 있다면?
            print(-1)        # 바로 -1 출력하고 종료
            exit()
        max_days = max(max_days, cell) # 가장 큰 노드 vs 현재 비교할 노드

# 익었다 기준을 1부터 시작했으므로 1을 뺴줘야 정확한 반복 횟수를 구할 수 있음
print(max_days - 1)

# [deque 라이브러리 쓰는 경우 정리]
# 일반 리스트 -> pop(0) 이후 뒤에 애들 다 앞으로 땡겨주는 작업이 내부적으로 진행됨 (데이터 클 때 터짐)
# deque(양방향 리스트) -> pop(0) 하면 이후 동작 필요X ( 시간 복잡도 O(1)  )