import sys

limit = 10001
is_prime = [True] * limit
is_prime[0] = is_prime[1] = False 
# 1과 2는 소수에 포함X

# 나머지 소수 아닌 애들 False로 끄는 동작
# (limit**0.5) 동작을 통해 시간 복잡도 n^2 을 Nlog(log N)로 줄임
for i in range(2, int(limit**0.5) + 1) :
    if is_prime[i] :
        for j in range(i*i, limit, i) :
            is_prime[j] = False

def solve() :
    case = int(sys.stdin.readline())

    for _ in range(case) :
        n = int(sys.stdin.readline())
    
        a = n // 2
        b = n // 2

        # 두 소수의 차이가 가장 작아야 하니까 
        # 원래수에 반토막 내고 하나는 1씩 증가시키고
        # 하나는 1씩 감소시키며 최초로 소수 조건 만족시키는지를 판단
        while True :
            if is_prime[a] and is_prime[b] :
                print(f"{a} {b}")
                break

            a -= 1
            b += 1

solve()