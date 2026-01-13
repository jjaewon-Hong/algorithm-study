# 옮겨야 할 원판의 개수 -> n
# 원판을 옮기기 시작할 기둥 -> start
# 원판을 최종적으로 옮겨야 할 목적지 기둥 -> end
# 경유지 기둥 -> temp

def hanoi(n, start, end, temp):
    if n == 1:
        print(start, end)
        return
    hanoi(n - 1, start, temp, end)
    print(start, end)
    hanoi(n - 1, temp, end, start)

n = int(input())
print(2**n - 1) # 시간 복잡도 2^n
hanoi(n, 1, 3, 2) 

# n개의 원판이 있고
# 첫번째 기둥에서 세번째 기둥으로 옮겨라 
# 경유지는 2번 기둥임

# *[n=3기준 하노이 로직 이미지 추가함]*
