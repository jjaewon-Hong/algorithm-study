import sys
# count0, count1을 배열을 각각 두어 0의 개수와 1의 개수를 기억하는 방식

# N의 범위에 맞게 배열 생성, 일단 모두 0으로 초기화
count0 = [0] * 41
count1 = [0] * 41

count0[0], count1[0] = 1, 0 # 피보나치[0] 초기화
count0[1], count1[1] = 0, 1 # 피보나치[1] 초기화

for i in range(2, 41): # 피보나치[2] ~ 피보나치[40] 초기화
    count0[i] = count0[i-1] + count0[i-2]
    count1[i] = count1[i-1] + count1[i-2]

T = int(sys.stdin.readline())
if T:
    for _ in range(T):
        N = int(sys.stdin.readline())
        print(count0[N], count1[N]) 
        # 여러 인자를 쉼표로 구분하면 공백 하나 두고 출력

#def fibonacci(num) :
#    if num == 0 :
#        count0 += 1
#    elif num == 1 :
#        count1 += 1
#    else :
#        fibonacci(num-1) + fibonacci(num-2)
#    return count0, count1

# 피보나치 공식 그대로 살려서 이용하려 했지만
# count0, count1을 밖에 선언하면 안에서 함수 내에서 변수 인식을 못하고
# 함수 내부 맨위에 count0=0 count1=0 하면 계속 0으로 초기화 하므로 재귀 의미가 없어짐



