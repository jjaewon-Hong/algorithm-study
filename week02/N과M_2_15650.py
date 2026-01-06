import sys

def factorial(num):
    if num <= 0: return 1
    result = 1
    for i in range(num, 0, -1):
        result *= i
    return result

def combination(num1, num2):
    if num1 < num2 or num2 < 0: return 0
    return factorial(num1) // (factorial(num1 - num2) * factorial(num2))

try:
    N, M = map(int, sys.stdin.readline().split())
except:
    sys.exit()

if not (1 <= M <= N <= 8):
    sys.exit()

total_count = combination(N, M)

for k in range(total_count):
    temp_k = k
    low = 1

    for i in range(M):
        for j in range(low, N + 1):
            count = combination(N-j, M-1-i)
            # count구현에서 막힘 -> 뒤로 갈수록 줄어드는 수치
            # 'N-j'는 현재숫자 j를 썼으므로 남은 숫자
            # 'M-1-i'는 현재 i번째 자리를 채웠으므로, 선택 가능한 남은 숫자의 개수

            if temp_k < count:
                print(j, end=" ")
                low = j + 1
                break
            else:
                temp_k -= count
    print()