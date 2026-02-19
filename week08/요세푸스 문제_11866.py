import sys

n, k = map(int, sys.stdin.readline().split())
result = []

n_list = []
for i in range(1,n+1) :
    n_list.append(i)

while True :
    if len(result) == n :
        break

    for i in range(k-1) :
        n_list.append(n_list.pop(0))
    result.append(n_list.pop(0))

print("<", end="")
for i in result :
    print(i, end="")
    if i == result[-1] :
        continue
    print(end = ", ")
print(">")
        
