#팩토리얼 식을 먼저 구현
#n!에다 (n-m)! 과 m!로 나누어줌
import sys

def factorial(num):
    result = 1
    for i in range(num, 0, -1):
        result *= i
    return result 

def combination(num1, num2):
    return factorial(num1) // (factorial(num1-num2) * factorial(num2))

try:
    M,N = map(int, input().split())
    print(combination(M,N))
except ValueError:
    sys.exit()