#유클리드 호제법 사용 -> 나머지가 0이 될때 까지 반복
import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
if len(M_list) != M or len(N_list) != N :
    sys.exit()

#유클리드 호제법
def gcd(a,b) :
    while b > 0 :
        a,b = b, a%b
    # temp = a%b
    # a = b
    # b = temp
    return a

sum1 = sum2 = 1
for item in N_list :
    sum1 *= item
for item in M_list :
    sum2 *= item

result = gcd(sum1, sum2)

if result > 999999999 :
    print(f"{result % 1000000000:09d}")
else :
    print(result)