import sys

result = 0

def pay() :
    N, M  = list(map(int, sys.stdin.readline().split()))
    # N -> 끊어진 기타줄 개수, M -> 기타줄 브랜드
    money = []
    global result

    for i in range(M) :
        money.append(list(map(int, sys.stdin.readline().split())))

    min_pack = float('inf')
    min_one = float('inf')
    for i in range(M) :
        if min_pack > money[i][0] :
            min_pack = int(money[i][0])
        
        if min_one > money[i][1] :
            min_one = int(money[i][1])

    for _ in range(2) :
        if N // 6 == 0 :
            result += min(min_pack, min_one * N)
            # 낱개만 사는게 가장 저렴한 경우
            # 패키지로 사는게 가장 저렴한 경우
            break
        else :
            if min_one*6 < min_pack : # 그냥 쌩으로 낱개 사는게 더 싼 경우
                result += (min_one*6) * (N//6)
            else :
                result += min_pack * (N//6)
            N = N % 6

pay()
print(result)
