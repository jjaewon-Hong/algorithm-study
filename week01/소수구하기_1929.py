# %%
#소수의 조건 : 2,3,5,7,11,13, ..
#일단 짝수는 2 제외 소수에 포함 불가
#나머지는 전부 홀수이지만, 홀수*홀수 형태로 생성된 수인 경우는 소수 포함 불가
import sys

try :
    M, N = map(int, input().split())
except ValueError:
    sys.exit()

if not (1 <= M <= N <= 1000000):
    sys.exit()

Pnum = []

for num in range(M,N+1):
    prime_check = False
    
    if num == 2:
       prime_check = True
    elif num > 2 and num %2 == 1:
        prime_check = True
        limit = int(num ** 0.5)
        for d in range(3, limit + 1, 2) :
            if num % d == 0 :
                prime_check = False
                break
        
    if prime_check == True:
        Pnum.append(num)
        
print(*Pnum, sep="\n")

# %%



