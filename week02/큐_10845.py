import sys

num = int(sys.stdin.readline())
queue = []

for _ in range (num) :
    k = sys.stdin.readline().split()

    if not k :
        continue
    
    cmd = k[0]
    
    match cmd :
        case "push" :
            queue.append(k[1])
        
        case "pop" :
            if not queue :
                print(-1)
            else :
                print(queue.pop(0))
                
        case "size" :
            print(len(queue))

        case "empty": 
            # 파이썬에는 조건 ? T : F 형태의 삼항연산자 없음
            if not queue :
                print(1)
            else :
                print(0)

        case "front" :
            if not queue :
                print(-1)
            else :
                print(queue[0])
                

        case "back" :
            if not queue :
                print(-1)
            else :
                print(queue[-1])
                        