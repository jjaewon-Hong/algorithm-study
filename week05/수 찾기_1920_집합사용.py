# [집합 사용하여 메모리 초과 문제 해결]
import sys

N = int(sys.stdin.readline())
N_set = set(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

for x in M_list :
    if x in N_set :
        print(1)
    else :
        print(0)

"""
[메모리 초과]
N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

total_max = max(max(N_list), max(M_list))
graph = [0] * (total_max+1)

for i in N_list :
    graph[i] = 1

for x in M_list:
    if graph[x] == 1 :
        print(1)
    else :
        print(0)
"""          
    