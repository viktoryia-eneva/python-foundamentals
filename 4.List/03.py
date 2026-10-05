n = int(input())

i = 0
posCount = 0
negativeCount = 0
posList = []
negList = []
sum = 0

while i < n:
    numbers = int(input())

    if numbers >= 0:
        posCount += 1
        posList.append(numbers)
    else:
        negativeCount += 1
        negList.append(numbers)
        sum += numbers

    i += 1

print(posList)
print(negList)
print("Count of positives: ", posCount)
print("Count of negatives: ", negativeCount)
print("Sum of negatives: ", sum)