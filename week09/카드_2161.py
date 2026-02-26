import sys
from collections import deque

def solve():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    n = int(input_data)

    cards = deque(range(1, n + 1))
    result = []

    while len(cards) > 1:
        result.append(cards.popleft())
        cards.append(cards.popleft())
    result.append(cards[0])


    output = ' '.join(map(str, result))
    print(output)

solve()