#[가능한 행동]
# 1) 한주 매수 
# 2) wait 
# 3) 전량 매도(미래를 알고있는 상황 -> 부분 매도 고려할 필요X) 
import sys

def solve() :
   T = int(sys.stdin.readline())

   for _ in range(T) :
        N = int(sys.stdin.readline())
        prices = list(map(int, sys.stdin.readline().split()))

        profit = 0
        max_price = 0

        for i in range(N-1, -1, -1) : 
            # 역방향 탐색으로 세가지 상황 모두 반영해버림 => 날마다 내려간다면 profit은 0
            if prices[i] > max_price : # 오늘 가격이 미래 가격일 보다 비싸다라고 거르는 과정
                max_price = prices[i]
                # max_price 가 업데이트 되는 순간 전량 매도 (3)
                # if문 연속 동작일때 아무 변화X => wait (2)
                 
            else : # 오늘 가격이 미래 가격일과 같거나 싸다고 판단
                profit += (max_price - prices[i]) 
                # max_price인 날 팔기 위해 매수 (1)
                # max_price와 현재가 같은 경우 아무 변화X => wait (2)

        print(profit)

solve()

"""
[오류코드 -> 아무것도 안하는 경우 반영X, 마지막날 팔고 나머지 날은 사는 특정한 경우만 성립]
import sys

def solve() :
   T = int(sys.stdin.readline())

   for _ in range(T) :
        N = int(sys.stdin.readline())
        prices = list(map(int, sys.stdin.readline().split()))

        total = 0
        for i in range(N-1) : 
           total += prices[i]

        profit = prices[N-1] * N - total 
        print(profit)

solve()
"""

