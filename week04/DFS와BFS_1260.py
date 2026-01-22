# DFS 핵심구조 : 한길로 쭉 들어가는 구조 -> 스택 or 재귀 사용
# BFS 핵심구조 : 가까운 곳 모두 방문하고 그 다음으로 넘어감 -> 큐 사용


import sys
def dfs(idx) :
    global visited
    visited[idx] = True
    print(idx, end = ' ')
    for next in range(1, N+1) :
        if not visited[next] and graph[idx][next] : 
            # 아직 방문 안했고 현재 상태에서 갈수 있다면
            dfs(next) # 방문하러 가라

def bfs():
    global queue, visited
    while queue:
        cur = queue.pop(0)
        print(cur, end = ' ')
        for next in range(1, N+1) :
            if not visited[next] and graph[cur][next] :
                visited[next] = True
                queue.append(next)

# <<<< 0. 입력 및 초기화 >>>>
input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[False] * (N+1) for _ in range(N + 1)] 
# 0으로 채워진 (N+1) * (N+1) 크기의 배열
visited = [False] * (N + 1)

# <<<< 1. graph 정보 입력 >>>>
for _ in range(M) :
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True
    # ex) '1 2' 연결이 곧 '2 1'이라는 특성을 고려한 그래프

# <<<< 2. dfs >>>>
dfs(V) # 1부터 탐색 시작하자
print()

# <<<< 3. bfs >>>>
visited = [False] * (N + 1)
queue = [V]
visited[V] = True
bfs()

