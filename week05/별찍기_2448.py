import sys

def draw_stars(n) :
    if n == 3:
        return [" * ", " * * ", "*****"]
    
    stars = draw_stars(n//2)
    L = []

    for s in stars:
        L.append(" " * (n//2) + s + " " * (n//2))

    for s in stars:
        L.append(s + " " + s)

    return L

N = int(sys.stdin.readline())

result = draw_stars(N)
print("\n".join(result))