factor = int(input())
count = int(input())

i = 1
result = []

while i <= count:
        num = factor * i
        result.append(num)

        i += 1

print(result)