# [이분 탐색 사용하여 해결]
import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
N_list.sort()

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

def solve(m, N_list) : # m은 M_list의 요소
    low = 0
    high = len(N_list) - 1

    while low <= high :
        mid = (low + high) // 2

        if N_list[mid] == m :
            return 1
        elif N_list[mid] < m  :
            low = mid + 1
        else :
            high = mid - 1

    return 0

for m in M_list :
    print(solve(m, N_list))
   
        