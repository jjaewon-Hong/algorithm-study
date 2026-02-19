import sys
from collections import deque

def solve() :
    num = int(sys.stdin.readline()) # 테스트 케이스의 수

    for _ in range(num) :
        n, m = map(int, sys.stdin.readline().split())
        priorities = list(map(int, sys.stdin.readline().split()))
        queue = deque([(p,i) for i, p in enumerate(priorities)])
        # priorities에 [1, 2, 4, 3] 에 저장되어 있다고 가정하면
        # enumerate를 통해 [(1, 0), (2, 1), (4, 2), (3, 3)] 와 같은 형태로 처리

        count = 0

        while queue :
            current = queue.popleft()
            # 큐의 맨앞 요소 뽑아내고 

            if any(current[0] < item[0] for item in queue) :
                queue.append(current)
            # queue뒤쪽이랑 비교했을 때 더 큰거 있으면 현재 뽑은거 다시 맨 뒤에다 넣어버리고

            else :
                count += 1
                if current[1] == m:
                    print(count)
                    break
            # 아니라면 카운트 추가하다가 목표지점 만나면 그때 카운트 출력하고 중단          
            
solve()