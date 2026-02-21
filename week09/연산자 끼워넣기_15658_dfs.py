import sys

max_n = -float('inf')
min_n = float('inf')

def dfs(idx, total, plus, minus, mul, div, n, numbers, ops) :
    global max_n, min_n

    if idx == n :
        max_n = max(max_n, total)
        min_n = min(min_n, total)
        return
    
    if plus > 0 :
        dfs(idx+1, total + numbers[idx], plus - 1, minus, mul, div, n, numbers, ops)
    if minus > 0 :
        dfs(idx+1, total - numbers[idx], plus, minus - 1, mul, div, n, numbers, ops)
    if mul > 0 :
        dfs(idx+1, total * numbers[idx], plus, minus, mul - 1, div, n, numbers, ops)
    if div > 0 :
        # 파이썬에서 -3//2 를 하면 -2가 되는 내림 특성 떄문에 
        # / 를 사용하고 int 붙여 소수점 모두 버리게 함
        dfs(idx+1, int(total / numbers[idx]), plus, minus, mul, div -1, n, numbers, ops)
    
def solve() :
    n = int(sys.stdin.readline())
    numbers = list(map(int, sys.stdin.readline().split()))
    ops = list(map(int, sys.stdin.readline().split()))
    dfs(1, numbers[0], ops[0], ops[1], ops[2], ops[3], n, numbers, ops)

    print(max_n)
    print(min_n)

solve()