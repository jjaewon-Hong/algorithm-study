import sys
from collections import deque

# bfs인자 : 현재 행&열, 지도 높이&너비, 지도데이터, 방문기록
def bfs(y, x, h, w, graph, visited) : 
    # 8방향 -> 상 하 좌 우 + 대각선 4방향
    dy = [-1,1,0,0,-1,-1,1,1]
    dx = [0,0,-1,1,-1,1,-1,1]

    queue = deque([(y,x)])
    visited[y][x] = True

    while queue :
        cy, cx = queue.popleft()

        for i in range(8) :
            ny, nx = cy + dy[i], cx + dx[i]

            # if 1. 지도 범위에 있는 경우  
            # if 2. 땅인 경우 and 방문하지 않는 경우
            if 0 <= ny < h and 0 <= nx < w :    
                if graph[ny][nx] == 1 and not visited[ny][nx] :
                    visited[ny][nx] = True
                    queue.append((ny, nx))

while True :
    try :
        w,h = map(int, sys.stdin.readline().split())
        if w == 0 and h ==0 : # 입력이 없는 경우 반복문 탈출 시켜 종료
            break

        # 한줄에 n만큼 할당한 w*h 그래프 생성
        # 방문 여부 판별할 visited도 w*h 크기에 False로 채움 
        graph = [list(map(int, sys.stdin.readline().split())) for _ in range(h)]
        visited = [[False] * w for _ in range(h)]
        island_count = 0 

        for i in range(h) :
            for j in range(w) :
                # 그래프 전부 돌며 그래프는 1인데 visited는 0인 곳 bfs로 방문
                if graph[i][j] == 1 and not visited[i][j] :
                    bfs(i, j, h, w, graph, visited)
                    island_count += 1
        # 최초 조건문 들어갔을떄 연결된 거 싹다 visited는 true로 바꿔 다신 선택하지 못하게 막아둠
        # +1 된 형태로 다음 반복문 탐색시작 ( 조건문 만족하면 위와 같은 방식 그대로 진행)


        print(island_count)
    except EOFError :
        break
