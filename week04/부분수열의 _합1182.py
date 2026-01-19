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
    
    dfs(index + 1, new_sum)
    dfs(index + 1, current_sum)

dfs(0,0)
print(count)  