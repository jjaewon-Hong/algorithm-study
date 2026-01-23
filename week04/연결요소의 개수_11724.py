import sys
sys.setrecursionlimit(10**6) 
# 범위확장 (정점의 개수가 일반적으로 1000이하인데 넘는 경우 추가해줘야함 -> 1,000,000으로 확장)
input = sys.stdin.readline
N, M = map(int, input().split()) # 정점 개수, 간선 개수
 
graph = [[False] * (N+1) for _ in range(N + 1)] 
visited = [False] * (N + 1)

for _ in range(M) :
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

def dfs(idx) :
    global visited
    visited[idx] = True
    for next in range(1, N+1) :
        if not visited[next] and graph[idx][next] : 
            # 아직 방문 안했고 현재 상태에서 갈수 있다면
            dfs(next) # 방문하러 가라    

count = 0

for i in range(1, N+1) :
    if not visited[i] :
        count += 1
        dfs(i)

print(count)