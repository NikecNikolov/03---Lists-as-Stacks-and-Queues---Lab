from collections import deque


kids = deque(input().split())
number = int(input())

for i in range (0,number):
    while len(kids) > 1:

        if len(kids) > i:
            kids.rotate(-number)
            print(f'Removed {kids.pop()}')
        else:
            print(f'Removed {kids.pop()}')

print(f'Last is {kids.popleft()}')