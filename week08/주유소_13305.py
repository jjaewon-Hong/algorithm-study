# 맨 마지막 주유소 가격은 의미 없음 => 제외
# 가장 저렴한 주유소에서 최대한 숫자를 받아내고
# 나머지 주유소에서 최소한의 숫자만 -> 반례 : 5 2 7 1 처럼 가격이 배정된 경우가 성립이 안됨
import sys

def solve() :
    num = int(sys.stdin.readline())
    distance = list(map(int, sys.stdin.readline().split()))
    price = list(map(int, sys.stdin.readline().split()))

    dist = sum(distance)

    for i in range(num-1) :
        if dist == 0 :
            break
        
            
