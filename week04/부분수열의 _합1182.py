import sys

N, S = map(int, sys.stdin.readline().split()) # 5 0
nums = list(map(int, sys.stdin.readline().split())) # -7 -3 -2 5 8
count = 0

def dfs(index, current_sum) :
    global count 
    # 함수 밖 카운트를 읽을 수만 있고 원래 수정은 안되지만 global로 가능하게 함

    if index == N :
        return 
    
    new_sum = current_sum + nums[index]
    if new_sum == S:
        count += 1

    dfs(index + 1, new_sum) # 루트기준 좌측 가지 (현재숫자를 더함)
    dfs(index + 1, current_sum) # 루트기준 우측 가지 (현재숫자 더하지 않음)
    # -3부터 시작해서 5까지 더해지는 형태도 찾을 수 있게 함

dfs(0,0)
print(count)  
