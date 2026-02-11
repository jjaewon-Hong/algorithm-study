import sys

A, B = map(int, sys.stdin.readline().split())
max_num = float('inf') # 어떤 숫자와 비교해도 가장 작은 횟수를 뽑아내기 위함 

def dfs(current, count) :
    global max_num

    # 목표 B 도달 시 최솟값 갱신
    if current == B :
        max_num = min(max_num, count)
        return

    if current > B :
        return

    dfs(current * 2, count + 1) # 2곱함, count+=1
    dfs(current*10 + 1, count + 1) # 1을 오른쪽에 붙임, count+=1

dfs (A, 1)

if max_num == float('inf') :
    print(-1)
else :
    print(max_num)
