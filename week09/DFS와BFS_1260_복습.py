import sys

def dfs(idx) :
    global visited
    visited[idx] = True
    print(idx, end = " ")
    for next in range(1, N+1) :
        if not visited[next] and graph[idx][next] :
            dfs(next)

def bfs() :
    global visited
    while queue :
        cur = queue.pop(0)
        print(cur, end = " ")
        for next in range(1, N+1) :
            if not visited[next] and graph[cur][next] :
                visited[next] = True
                queue.append(next)

N, M, V = map(int, sys.stdin.readline().split())
# N 정점개수, M 간선개수, V 탐색시작번호
graph = [[False] * (N+1) for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(M) :
    a, b = map(int, sys.stdin.readline().spliㄴt())
    graph[a][b] = True
    graph[b][a] = True

dfs(V)
print()

visited = [False] * (N+1)
queue = [V]
visited[V] = True
bfs()