import sys

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
count = 0

def dfs(index, current_sum) :
    global count 
    # 함수 밖 카운트를 읽을 수만 있고 원래 수정은 안되지만 global로 가능하게 함

    if index == N :
        return
    
    new_sum = current_sum + nums[index]
    if new_sum == S:
        count += 1
    
    dfs(index + 1, new_sum) # 좌로 뻗어나간거에서 결과값 0이 있는지 확인이 필요함
    dfs(index + 1, current_sum) # 우로 뻗어나감 (new_sum은 어차피 초기화 될거니 맨 우측 가지 결과값 0인건 의미X)

dfs(0,0)
print(count)  
