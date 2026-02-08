import sys

def coin() :
    N, K = map(int, sys.stdin.readline().split())
    coin_list = []

    for i in range(N) :
        coin_list.append(int(sys.stdin.readline()))

    coin_list.sort(reverse = True)
    count = 0

    for i in coin_list :

        if i <= K :
            count += K//i 
            K -= i * (K//i)
            # 위에 두개의 식 순서 바뀌면 제대로 된 count 불가

    print(count) 

coin()           

