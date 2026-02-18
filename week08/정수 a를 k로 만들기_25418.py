import sys

a, k = map(int, sys.stdin.readline().split())
count = 0

while True :
    if a == k :
        break
    
    if k % 2 == 0 and k // 2 >= a :
        k //= 2
    else :
        k -= 1
    count += 1

print(count)
