import sys
num = int(sys.stdin.readline()) 
#데이터를 1000개 이상 정도로 많이 받을 때는 input 대신 씀 (시간 초과 오류)
stack = [] 

for _ in range(num) :
    k = sys.stdin.readline().split()

    if not k:
        continue

    cmd = k[0]

    if cmd == "push" :
        value = k[1]
        stack.append(value)

    elif cmd == "pop" :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack.pop())

    elif cmd == "top" :
        if len(stack) == 0 :
            print(-1)
        else :
            print(stack[-1])

    elif cmd == "empty" :
        if not stack :        # len(stack) == 0 :
            print(1)
        else :
            print(0)

    elif cmd == "size" :
        print(len(stack))