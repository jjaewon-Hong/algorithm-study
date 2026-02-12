# 오름차순 정렬 후 -> 값의 축적 계산 필요 
import sys

def solve() :
    num = int(sys.stdin.readline())
    time = list(map(int, sys.stdin.readline().split()))
    
    time.sort()

    temp = 0
    all_time = []

    for i in range(num) :
        temp += time[i]
        all_time.append(temp)

    result = 0

    for i in all_time :
        result += i

    print(result)

solve()
