# 맨 마지막 주유소 가격은 의미 없음 => 제외
# 가장 저렴한 주유소에서 최대한 숫자를 받아내고
# 나머지 주유소에서 최소한의 숫자만 -> 반례 : 5 2 7 1 처럼 가격이 배정된 경우가 성립이 안됨
import sys

def solve() :
    num = int(sys.stdin.readline())
    distance = list(map(int, sys.stdin.readline().split()))
    price = list(map(int, sys.stdin.readline().split()))

    cost = 0
    min_price = price[0]

    for i in range(num-1) :
        # 현재 주유소가 지금 값보다 싼 경우
        if price[i] < min_price :
            min_price = price[i]
        
        # 현재까지의 최저가로 이번 구간 이동
        cost += min_price * distance[i]
    print(cost)

solve()
        
            
