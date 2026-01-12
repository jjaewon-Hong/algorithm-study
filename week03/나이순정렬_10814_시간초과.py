import sys

num = int(input())
user = []
# 시간초과 오답 분석 -> 데이터가 N개 일때 약 N^2번의 비교를 수행
# 대표적인 시간 복잡도 N^2 개념
# 1. 선택 정렬 
# 2. 버블 정렬
# 3. 삽입 정렬 (실전에서 가끔 쓰이는 유일한 형태)


for _ in range (num) :
    data = sys.stdin.readline().split()

    age = int(data[0])
    name = data[1]
    user.append((age, name))

for x in range(num) :
    for y in range(x+1, num):
        if user[x][0] > user[y][0] :
            user[x], user[y] = user[y], user[x]

# 불안정 정렬 : 제 3의 요소로 인해 나이가 같은 경우에도 순서가 뒤집어져 출력될 가능성 존재 
for i in user :
    print(i[0], i[1])


    