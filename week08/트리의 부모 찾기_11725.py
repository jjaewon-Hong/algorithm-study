import sys
sys.setrecursionlimit(10**6) 
# 기본 재귀 깊이인 1000에서 제한 범위 늘려줌

def solve() :
    num = int(sys.stdin.readline())
    graph = [[] for _ in range(num+1)]

    for _ in range(num-1) :
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v) 
        graph[v].append(u)

    # graph[1] : [6]
    # graph[2] : [4]
    # graph[3] : [6, 5]
    # graph[4] : [1,2,7]
    # graph[5] : [3]
    # graph[6] : [1, 3]
    # graph[7] : [4]
    # => 각 배열의 맨 앞 요소가 부모 노드가 됨

    parent = [0] * (num + 1) # 결과 담을 바구니 준비

    def dfs(current) :
        for next in graph[current] :
            if parent[next] == 0 :
                parent[next] = current
                dfs(next)
            
    parent[1] = 1 # 무한루프 빠지는거 방지 
    dfs(1)

    print('\n'.join(map(str, parent[2:])))
    # join은 문자열 리스트 요소들 사이에 /n을 넣어서 하나의 문자열로 합침
    # map(str, ...) 해주는 이유

solve()