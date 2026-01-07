import sys

try :
    M,N = map(int, sys.stdin.readline().split())
except :
    sys.exit()


stack = []

def search(depth): #스택의 층
    if depth == N: #스택이 최대 층까지 도달하면 
        print(*stack)
        return
    
    for i in range(1, M+1) :
            stack.append(i)
            search(depth+1)
            stack.pop()
search(0)