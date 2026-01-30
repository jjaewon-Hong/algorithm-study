# 묶여 있는 색깔의 덩어리 개수를 카운트함
import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

white_cnt = 0
blue_cnt = 0

def cut_paper(x,y,N) :
    global white_cnt, blue_cnt

    check_color = paper[x][y] # 왼쪽 위부터 시작

    for i in range(x, x+N) : 
        # 결국 N번 도는건데 i와 같은 변수를 독립적으로 하나 더 확보하기 위함
        for j in range(y, y+N) :
            if paper[i][j] != check_color :
                half = N // 2

                # 재귀의 크기를 줄이기 위해 마지막에 half 인자 필요함
                # <<< 4방향이 포함만 된다면 순서 섞여도 상관 X >>>
                cut_paper(x, y, half) # 좌측위

                cut_paper(x, y + half, half) # 우측위 
                # (세로줄의 위치 조정이니까 우측이동임, 하단 이동 아님 주의)

                cut_paper(x + half, y, half) # 좌측아래

                cut_paper(x + half, y + half, half) # 우측아래

                return
            
    if check_color == 0:
        white_cnt += 1
    else :
        blue_cnt += 1

cut_paper(0, 0, N)

print(white_cnt)
print(blue_cnt)

"""" [분할정복 기본 템플릿]
def merge(left, right) :
    result = []
    while len(left) > 0 or len(right) > 0:

        return result

def solve(data) :
    if len(data) <= 1 :
        return data
    
    mid = len(data) // 2
    left = solve(data[:mid])
    right = solve(data[mid:])

    return merge(left, right)
"""