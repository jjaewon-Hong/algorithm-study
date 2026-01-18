import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
lengths = [1] * N

for i in range(N) :
    for j in range(i) :
        if nums[j] > nums[i] :
            lengths[i] = max(lengths[i], lengths[j] + 1)

print(max(lengths))