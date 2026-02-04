import sys

def solve() :
    T = int(sys.stdin.readline())

    for _ in range(T) :
        N = int(sys.stdin.readline())
        height = list(map(int, sys.stdin.readline().split()))

        mid = N // 2
        tok = mid + 1
        height.sort()

        sorted_height = [0] * N
        left = 0
        right = N-1

        for i in range(N) : 
            # 양끝 좌우 왔다갔다하며 큰 값들부터 채워나가는 느낌
            if i % 2 == 0 :
                sorted_height[left] = height[i]
                left+=1
            else :
                sorted_height[right] = height[i]
                right -= 1

        max_gap = 0
        for i in range(N) :
            gap = abs(sorted_height[i] - sorted_height[(i+1) % N])
            # 마지막 인덱스 들어갈때 첫번째와 비교하기 위해 (i+1) % N 사용
            if gap > max_gap :
                max_gap = gap
        
        print(max_gap)

solve()
            
             