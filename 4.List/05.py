n = int(input())

i = 0
newList = []
numbers = []

while i < n:
    num = int(input())
    numbers.append(num)

    i += 1

rule = input()

if rule == "even":
        for number in numbers:
            if number % 2 == 0:
                newList.append(number)
elif rule == "odd":
        for number in numbers:
            if number % 2 != 0:
                newList.append(number)
elif rule == "negative":
        for number in numbers:
            if number < 0:
                newList.append(number)
elif rule == "positive":
        for number in numbers:
            if number >= 0:
                newList.append(number)

print(newList)