import sys

num = int(sys.stdin.readline())
state = sys.stdin.readline().strip()
data = [int(sys.stdin.readline()) for _ in range(num)]

stack = []

for char in state :
    if 'A' <= char <= 'Z' :
        stack.append(data[ord(char)-ord('A')])
        # ord는 문자를 해당 문자의 유니코드(숫자) 값으로 바꿔주는 함수
        # ex) ord('A') = 65 를 의미
    else :
        num1 = stack.pop()
        num2 = stack.pop()

        #후입 선출 규칙에 따라 num2를 num1보다 앞에 배치
        if char == '+' :
            stack.append(num2 + num1)
        elif char == '-' :
            stack.append(num2 - num1)
        elif char == '*' :
            stack.append(num2 * num1)
        elif char == '/' :
            stack.append(num2 / num1)

print(f"{stack[0]:.2f}")            