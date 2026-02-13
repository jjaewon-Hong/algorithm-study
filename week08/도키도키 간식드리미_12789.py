import sys

def solve() :
    num = int(sys.stdin.readline())
    turn = list(map(int, sys.stdin.readline().split()))
    
    sequence = 1
    stack = [] # 결과 담는 배열

    for i in turn :
        stack.append(i)
        
        while stack and stack[-1] == sequence :
            stack.pop()
            sequence += 1

    if not stack :
        print("Nice")
    else :
        print("Sad")

solve()