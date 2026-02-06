import sys

n = int(sys.stdin.readline())

rope_list = [0] * n 

for i in range(n) :
    rope_list[i] = int(sys.stdin.readline())

rope_list.sort(reverse = True)

result = []

for i in range(n) :
    result.append(rope_list[i] * (i+1))
    # 점점 낮아지는 중량 * 점점 늘어나는 로프 수
    # 반복문 처음 : 하나의 중량이 압도적으로 크면 그냥 이거 하나쓰는게 나음 (나머지 억지로 쓰는거 보다)
    # 반복문 끝 : 로프가 끊이지 않되 로프를 가장 많이 사용하여 들 수 있는 값
        
print(max(result))
    





