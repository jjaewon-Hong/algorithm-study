# A의 최솟값이 B의 최댓값에 대칭 시켜주면됨
# 그리고 A * B 한 값들 각각 더해서 출력
import sys

def solve() :
    num = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    A.sort()
    B.sort(reverse = True)
    result = 0

    for i in range(num) :
        result += A[i] * B[i]

    print(result)

solve()
