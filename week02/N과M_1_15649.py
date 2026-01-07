#핵심 키워드 : 
# DFS
# 상태공간 트리
# guard (들어갈수 있는 숫자 리스트)
# 상태 복구 (재귀로 인해 후순위로 밀렸던 pop동작)
import sys

try :
    M,N = map(int, sys.stdin.readline().split())
except :
    sys.exit()

if not (1<=M<=N<=8) :
    sys.exit()

guard = [False] * (M + 1)
stack = []

def search(depth): #스택의 층
    if depth == N: #스택이 최대 층까지 도달하면 
        print(*stack)
        return
    
    for i in range(1, M+1) :
        if not guard[i] :
            guard[i] = True
            stack.append(i)

            search(depth+1)

            stack.pop()
            guard[i] = False

search(0)