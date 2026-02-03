# 분할 정복
import sys

N = int(sys.stdin.readline())
matrix = [list(sys.stdin.readline().strip()) for _ in range(N)]


def solve(y,x,n) :
    check = matrix[y][x]
    is_same = True

    # 노드 하나씩 탐색하며 반복문 탈출 조건을 만듦
    for i in range(y, y+n) :
        for j in range(x, x+n) :
            if matrix[i][j] != check:
                is_same = False
                break
        if not is_same:
            break
        
    
    if is_same :
        print(check, end="")
    else:
        print("(", end="") #쪼개기 시작

        new_n = n // 2
        solve(y, x, new_n) # 왼쪽 위
        solve(y, x+new_n, new_n) # 오른쪽 위
        solve(y + new_n, x, new_n) # 왼쪽 아래
        solve(y + new_n, x + new_n, new_n) # 오른쪽 아래

        print(")", end="") #쪼개기 마무리

solve(0, 0, N)