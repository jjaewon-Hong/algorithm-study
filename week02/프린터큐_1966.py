import sys

num = int(sys.stdin.readline())

for _ in range(num):
    N, M = map(int, sys.stdin.readline().split())
    priorities = list(map(int, sys.stdin.readline().split()))
    
    queue = [(val, idx) for idx, val in enumerate(priorities)]
    # priorities가 2143인 경우에 enmurate는 (0,2) (1,1) (2,4) (3,3) 형태로 저장
    count = 0 
    
    while True:
        current = queue.pop(0)
        
        if any(current[0] < x[0] for x in queue):
            # 현재 기준으로 뒤에 중요도가 높은 것이 있는지 확인하는 조건
            queue.append(current)
        else:
            count += 1
            if current[1] == M:
                print(count)
                break