import sys

N = int(sys.stdin.readline())
SB = []

for i in range(N) :
    SB.append(list(map(int, sys.stdin.readline().split())))

result = float('inf')

def dfs(idx, sour, bitter, count) : 
    # 전체 탐색을 위한 idx
    # 넣을 재료를 세기 위한 count
    global result

    if idx == N :
        if count > 0 :
            result = min(result, abs(sour - bitter)) 
            # 모든경우의 수 중에서 신맛-쓴맛 차이가 가장 작은값 
        return
    
    # 선택 1: 현재 재료를 포함
    dfs(idx + 1, sour * SB[idx][0], bitter + SB[idx][1], count + 1)
    # SB[idx][0] -> 신맛, SB[idx][1] -> 쓴맛

    # 선택 2: 현재 재료 X
    dfs(idx + 1, sour, bitter, count) 
    

dfs(0, 1, 0, 0) 
# 신맛에 최초에 곱해야 하니 2번째 인자 1로 잡음
# 쓴맛에 최초에 더해야 하니 3번째 인자 0으로 잡음
print(result)


        

       