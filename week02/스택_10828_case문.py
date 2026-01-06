import sys

num = int(sys.stdin.readline())
stack = []

for _ in range(num) :
    k = sys.stdin.readline().split()

    if not k :
        continue

    cmd = k[0]

    match cmd:
        case "push" :
            value = k[1]
            stack.append(k[1])
        
        case "pop" :
            if len(stack) == 0 :
                print(-1)
            else :
                print(stack.pop())
        
        case "size" :
            print(len(stack))

        case "empty" :
            if not stack :
                print(1)
            else :
                print(0)
        
        case "top" :
            if not stack :
                print(-1)
            else :
                print(stack[-1])