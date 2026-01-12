import sys

num = int(input())
user = []

for _ in range (num) :
    data = sys.stdin.readline().split()

    age = int(data[0])
    name = data[1]
    user.append((age, name))

for x in range(num) :
    for y in range(x+1, num):
        if user[x][0] > user[y][0] :
            user[x], user[y] = user[y], user[x]

for i in user :
    print(i[0], i[1])
    
    



    