# 오답1 : 파이썬에서 비교구문 (수정완료) 
# && -> and, || -> or, ! -> not
# !=는 존재
# 오답2 : max_num 에서 -1씩 뺴는 과정에서 시간 초과 오류 발생
import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))
if len(M_list) != M or len(N_list) != N :
    sys.exit()

sum1 = sum2 = 1

for item in N_list :
    sum1 *= item
for item in M_list :
    sum2 *= item

max_num = sum1 if sum1<sum2 else sum2
result = 1

for k in range (max_num, 0, -1) :
    if sum1%k  == 0 and sum2%k == 0 :
        result = k
        break

print(result)

