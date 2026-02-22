import sys
from collections import deque

def solve() :
    N, M = list(map(int, sys.stdin.readline().split()))

    adj = [[] for _ in range(N+1)]
    # 숫자 담는데 헷갈리지 않게 +1 여유 있게 받아둠

    idx = 2
    for _ in range(M) :
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        idx += 2
    # adj 배열에 (x,y)와 (y,x)로 담음

    def bfs(start_node) :
        distances = [-1] * (N+1)  
        # 방문하지 않았음을 표시하기 위해 -1
        # 일반 visited와 다르게 방문 여부 + 시작점으로 부터의 거리 정보도 포함함
        queue = deque([start_node])
        distances[start_node] = 0 # 시작점 거리는 0 -> 방문 완료

        while queue :
            curr = queue.popleft() # 현재 조사 대상 뽑아냄
            for neighbor in adj[curr] : # 친구 목록 확인하고
                if distances[neighbor] == -1 : # 방문하지 않았다면
                    distances[neighbor] = distances[curr] + 1 # 거리기록 함
                    queue.append(neighbor)

        return sum(d for d in distances if d > 0) 
        # distances에서 하나씩 돌며 d에 담고
        # 그중 d > 0 인 경우만 고른값들을 모두 더함
    
    # bfs내부에서는 queue에다가 다 담아 정리하고 
    # 그 결과 출력 자체는 result에 담아서 출력하는 느낌
    result = []
    for i in range(1, N+1) :
        result.append((bfs(i), i))

    print(min(result)[1]) 

solve()