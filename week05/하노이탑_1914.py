import sys

def hanoi(n, start, end , temp) :
    if n == 1 :
        print(start, end) 
        return
    hanoi(n-1, start, temp, end) 
    print(start, end)
    hanoi(n-1, temp, end, start)

input = sys.stdin.readline
n = int(input())

print(2**n - 1)

if n<= 20 :
    hanoi(n, 1, 3, 2)