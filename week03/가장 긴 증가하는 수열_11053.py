# 가장 긴 증가하는 수열
# 조건1 -> 뒤의 숫자가 앞의 숫자보다 큰 경우만 카운트 함 (증가수열)
# 10 20 11 12 와 같은 경우,
# 카운트 변수 하나만으로 모든 경우의 수 기억 못함
# 조건2 -> 일단 카운트를 배열 형태로 받자 (가장 긴걸 찾아내야함)

import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
lengths = [1] * N

for i in range(N) :
    for j in range(i) :
        if nums[j] < nums[i] :
            lengths[i] = max(lengths[i], lengths[j] + 1)

print(max(lengths))
            
