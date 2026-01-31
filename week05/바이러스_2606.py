import sys

N = int(sys.stdin.readline())
V = int(sys.stdin.readline())
graph = [[0] * (N+1) for _ in range(N+1)]
visited = [False] * (N + 1)

for _ in range(V) :
    a,b = list(map(int, sys.stdin.readline().split()))
    graph[a][b] = graph[b][a] = 1

def dfs(idx) :
    global visited
    visited[idx] = True
    for next in range(1, N+1) :
        if not visited [next] and graph[idx][next] :
            dfs(next)

dfs(1)

print(visited.count(True) - 1)

"""def dfs(idx) : # 재귀
    global visited
    visited[idx] = True
    print(idx, end = ' ')
    for next in range(1, N+1) :
        if not visited[next] and graph[idx][next] : 
            # 아직 방문 안했고 현재 상태에서 갈수 있다면
            dfs(next) # 방문하러 가라

def bfs(): # 큐
    global queue, visited
    while queue:
        cur = queue.pop(0)
        print(cur, end = ' ')
        for next in range(1, N+1) :
            if not visited[next] and graph[cur][next] :
                visited[next] = True
                queue.append(next)
"""