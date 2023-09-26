from collections import deque
string = input()
Stack = deque()
while string != "End":
    if string != "Paid":
        Stack.append(string)
    else:
        while Stack:
            print(Stack.popleft())

    string = input()
print(f'{len(Stack)} people remaining.')