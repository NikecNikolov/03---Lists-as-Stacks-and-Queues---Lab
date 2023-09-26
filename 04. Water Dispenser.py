from collections import deque
quantity = int(input())
users = deque()

start = ""
entersplitted = []
while True:
    enter = input()
    entersplitted = enter.split(' ')
    if enter == "End":
        break
    elif enter == "Start" and start == "":
        start = "Start"
    elif start == "Start" and enter != "Start":
        if entersplitted[0] == "refill":
            quantity += int(entersplitted[1])
        else:
            if quantity < int(enter):
                print(f'{users.popleft()} must wait')
            else:
                quantity -= int(enter)
                print(f'{users.popleft()} got water')
    else:
        users.append(enter)
print(f'{quantity} liters left')