import sys

def solve() :
    L, R = sys.stdin.readline().split()

    if len(L) != len(R) :
        print(0)
        return
    
    min_8 = 0
    for i in range(len(L)) :
        if L[i] == R[i] :
            if L[i] == '8' :
                min_8 += 1
        else :
            break

    print(min_8)
    
solve()

