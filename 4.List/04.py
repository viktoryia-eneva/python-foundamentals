n = int(input())
word = input()
strings = []

i = 0

while i < n:
    string = input()
    strings.append(string)

    i += 1

print(strings)

for i in range(len(strings) - 1, -1, -1):
    element = strings[i]
    if word not in element:
        strings.remove(element)
print(strings)