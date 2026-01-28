# F -> 건물 전체 층수
# G -> 스타트링크 (목적지)
# S -> 현재위치
# BFS로 접근
import sys
from collections import deque
F, S, G, U, D = list(map(int, sys.stdin.readline().split()))
count = 0

def bfs() :
    queue = deque([S]) # 큐 생성 및 시작점 추가

    visited = [0] * (F+1)
    visited[S] = 1 # 횟수를 1로 시작하고 나중에 1뺴줌

    while queue:
        cur = queue.popleft()

        if cur == G:
            return visited[cur] - 1 # 목적지에 도달했을 때 종료
        
        for next_floor in (cur + U, cur - D) : 
            if 1 <= next_floor <= F and visited[next_floor] == 0 : 
                # 안갔던 곳이 실제 있는 건물 층수라면 실행시켜라
                visited[next_floor] = visited[cur] + 1
                # 다음 층수에 '현재+1' 숫자로 채워 넣음
                queue.append(next_floor) # 큐에 쌓음 (위 아래로 일단 다 뻗어나가는 형태)

    return "use the stairs"

print(bfs())