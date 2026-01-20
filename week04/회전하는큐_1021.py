#left_move인 경우 맨 앞에 요소가 맨 뒤로 감
#right_move인 경우 맨 뒤에 요소가 맨 앞으로 감
import sys

N, M = map(int, sys.stdin.readline().split())
targets = list(map(int, sys.stdin.readline().split()))

queue = [i for i in range(1, N+1)] 
# for i in range(1,N)과 다르게 i 값을 리스트에 담음

count = 0

for target in targets : #targets 함수 포함된거 처리할때까지 반복
    idx = queue.index(target) # 첫번째 요소를 얻고자 할떄 1이 자동으로 idx에서 0으로 저장됨

    # 최솟값을 얻어내기 위해 좌,우 방향 모두 고려하여 처리하기 위함
    left_move = idx
    right_move = len(queue) - idx

    
    if left_move <= right_move :  
        count += left_move
    else :                      
        count += right_move
    
    queue = queue[idx:] + queue[:idx]
    # idx 포함해서 뒤부터 끝까지 잘라 먼저 붙임 (이상)
    # idx 포함하지 않고 앞까지 잘라 뒤에 붙임 (미만)
    # => 뽑고자 하는 idx가 맨앞에 있음
    
    queue.pop(0)  # 맨앞의 idx만 딱 뽑아냄

print(count)