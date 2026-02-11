import sys
from collections import deque

def solve() :
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())

    board = [[0] * (n+1) for _ in range(n+1)] # 보드 크기 할당
    for _ in range(k) : # 사과 좌표 할당
        r, c = map(int, sys.stdin.readline().split())
        board[r][c] = 2

    l = int(sys.stdin.readline()) # 방향 몇 번 틀것인지 할당 
    times = {}
    for _ in range(l) : # 뱀 x초 뒤, c로 방향 전환 
        x, c = sys.stdin.readline().split()
        times[int(x)] = c

    # 방향 설정 (우, 하, 좌, 상)
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y = 1, 1 # 맨위 맨좌측에서 시작 => 뱀의 시작 위치는 (1, 1)
    board[x][y] = 1 # 뱀이 있는 자리는 1로 표시
    direction = 0 # 처음에는 오른쪽(index 0)을 보고 시작
    time = 0 # 게임 경과 시간
    snake = deque([(x, y)]) 
    # 뱀의 몸통 좌표들을 담는 큐 (새로운 머리가 뒤에 생김, 오래된 꼬리 잘림)

    while True :
        time += 1 # 1초 경과

        # 다음 칸 계산
        nx = x + dx[direction]
        ny = y + dy[direction]

        # 벽에 부딪히거나 자신의 몸(1)에 부딪히는지 확인
        if 1 <= nx <= n and 1 <= ny <= n and board[nx][ny] != 1 :
            # 사과가 없는 칸(0)이면
            if board[nx][ny] == 0 :
                # 꼬리를 줄여서 이동을 완성함
                tx, ty = snake.popleft() # 가장 예전에 들어온 좌표(꼬리)를 꺼냄
                board[tx][ty] = 0 # 보드에서 꼬리 제거

            # 사과가 있든 없든 머리는 새 칸으로 이동
            board[nx][ny] = 1 # 보드에 새 머리 위치 표시
            snake.append((nx, ny)) # 뱀 큐에 새 머리 좌표 추가
            x, y = nx, ny # 현재 머리 위치 업데이트

            # 방향 전환 확인 (현재 시간이 방향 전환 예약 시간인지)
            if time in times :
                if times[time] == 'D' : # # 'D'면 시계방향 90도 회전
                    direction = (direction + 1) % 4
                else : # 'L'이면 반시계방향 90도 회전
                    direction = (direction - 1) % 4
        
        # 벽이나 몸에 부딪혔다면 게임 종료
        else :
            break

    print(time) # 최종 생존 시간 출력

solve()