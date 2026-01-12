import sys

n = int(sys.stdin.readline())
members = [[] for _ in range(201)]

for _ in range(n):
    info = sys.stdin.readline().split()
    age = int(info[0])
    name = info[1]
    members[age].append(name) # 나이와 이름이 순서대로 쌓임

for age in range(1, 201):
    for name in members[age]:
        sys.stdout.write(str(age) + " " + name + "\n")

# print는 
# 1. 입력받은값 문자열로 바꾸고
# 2. 여러 인자 사이 공백 띄우고 마지막 줄바꿈

# sys.stdout.write는
# 들어온 문자열 화면으로 그대로 보냄 
# (속도가 매우 빠름 -> 데이터 클 때 유용)

# 시간복잡도 O(N + K) 
# -> N번 반복하며 이름추가 및 나이범위 만큼 돌며 이름 출력
# => 나이 범위가 200이라 O(N)에 수렴