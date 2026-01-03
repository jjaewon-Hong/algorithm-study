# 입력을 받아 스택의 크기
# guard를 통해 스택에 해당 숫자가 입장이 가능한지 불가능한지 판단

num = int(input())
guard = [False] * (num)
stack = []

def search(depth):
    if depth == num:
        print(*stack)
        return
    
    for i in range(num):
        if not guard[i]:
            guard[i] = True
            stack.append(i+1)

            search(depth + 1)

            stack.pop()
            guard[i] = False

search(0)
