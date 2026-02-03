# 이분 탐색
import sys

def solve() :
    try :
        line1 = sys.stdin.readline().split()
        if not line1:
            return
        N, C = map(int, line1)

        houses = []
        for _ in range(N) :
            houses.append(int(sys.stdin.readline()))
    except ValueError:
        return

    houses.sort() # 내림차순 하려는 경우 houses.sort(reverse=True)

    start = 1
    end = houses[-1] - houses[0]
    result = 0

    while start <= end :
        mid = (start + end) // 2 # 임의의 공유기 간 최소 거리

        current = houses[0]
        count = 1

        for i in range(1, N) :
            if houses[i] >= current + mid :
                # 비교값을 평균으로 잡으면 안되는 이유
                # 1) 한쪽으로 값이 쏠린경우 매우 식이 길어짐
                # 2) 평균으로 구한 값이 집의 위치가 아니라면 허공의 시뮬레이션 우려
                count += 1
                current = houses[i]

        if count >= C:
            start = mid + 1
            result = mid
        else :
            end = mid - 1

    print(result)

solve() 
