import sys

nums = list(map(int, sys.stdin.readline().strip()))

for i in range(len(nums)) :
    for j in range(i) :
        if nums[i] > nums[j] :
            nums[i],nums[j] = nums[j],nums[i]


for i in nums:
    print(i, end="")