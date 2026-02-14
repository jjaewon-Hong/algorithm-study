import sys

def solve():
    num = int(sys.stdin.readline())
    turn = list(map(int, sys.stdin.readline().split()))
    
    sequence = 1
    stack = []  # 옆길 
    spare = []  # 간식을 받은 사람들을 순서대로 담는 곳
    
    for i in turn:
        stack.append(i)

        while stack and stack[-1] == sequence:
            person = stack.pop()
            spare.append(person)
            sequence += 1 

    answer = [n for n in range(1, num + 1)]

    if spare == answer:
        print("Nice")
    else:
        print("Sad")

solve()