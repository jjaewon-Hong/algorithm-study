import sys

def solve() :
    ex = sys.stdin.readline().strip().split('-')
    # '-' 를 기준으로 나눔
    
    result = 0

    # '-' 이전의 숫자들 처리 => - 는 다 뗐으니 + 기준으로 나누고 더하면 됨
    group = ex[0].split('+')
    for num in group :
        result += int(num)

    # 각 덩어리들을 통쨰로 빼줌 (두 번째 덩어리 부터 진행하면 됨)
    for group in ex[1:] :
        sub_sum = sum(map(int, group.split('+')))
        result -= sub_sum

    print(result)

solve()
