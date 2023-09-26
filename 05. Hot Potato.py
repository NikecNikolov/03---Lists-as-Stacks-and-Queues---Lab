string = input().split()

output_string = []

while string:
    output_string.append(string.pop())

print(' '.join(output_string))