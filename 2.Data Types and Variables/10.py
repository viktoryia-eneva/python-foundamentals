numberLines = int(input())

sum = 0

for i in range(1, numberLines + 1):
    char = input()
    sum += ord(char)

print(f"The sum equals: {sum}")