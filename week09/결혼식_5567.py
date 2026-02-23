import sys
from collections import deque

def solve() :
    try :
        num = int(sys.stdin.readline())
        m = int(sys.stdin.readline())
    except EOFError :
        return
    
    # 인접 리스트 구성
    adj = [[] for _ in range(num + 1)]
    for _ in range(m) :
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)

    distances = [-1] * (num+1) # 모든 사람거리 -1로 초기화
    queue = deque([1]) # 1번(상근이)부터 bfs 시작을 알림 
    distances[1] = 0 # 상근이 거리는 0으로 설정 (상근이와 상근이의 거리 /// 일단 -1은 아님)

    count = 0
    while queue :
        curr = queue.popleft()

        # bfs의 거리는 2까지만 탐색
        if distances[curr] == 2 :
            continue

        for neighbor in adj[curr] :
            if distances[neighbor] == -1 : # 첫 방문일 때
                distances[neighbor] = distances[curr] + 1
                queue.append(neighbor)
                count += 1 # 새로 발견한 친구 or 친구의 친구 카운트

    print(count)

solve()
    