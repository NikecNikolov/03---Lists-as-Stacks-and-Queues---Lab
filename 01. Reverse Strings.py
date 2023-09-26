string = list(input())
output = []

while len(string) > 0:
    output.append(string.pop())

print(''.join(output))