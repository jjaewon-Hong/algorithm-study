import sys

def draw_stars(n) :
    if n == 3:
        return ["  *  ", " * * ", "*****"] # 최초 n==3일 때 즉시 종료하며 n이 6일때 뿌림
        # 다섯칸 유지 
    
    stars = draw_stars(n//2)
    L = []

    #최초 n=3인 경우에는 밑에 for문 실행못시키고 사실상 n=6일 때 처음으로 for문 진입
    for s in stars: 
        L.append(" " * (n//2) + s + " " * (n//2)) 

    for s in stars:
        L.append(s + " " + s)

    return L

N = int(sys.stdin.readline())
print("\n".join(draw_stars(N)))