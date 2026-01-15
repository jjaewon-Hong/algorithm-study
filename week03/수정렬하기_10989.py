import sys

num = int(sys.stdin.readline())
count = [0] * 10001

for _ in range (num) :
    n = int(sys.stdin.readline())
    count[n] += 1

for i in range (10001):
    if count[i] != 0 :
        for _ in range(count[i]) :
            print(i)
    