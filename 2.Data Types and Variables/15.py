number = int(input())

i = 1
highestValue = 0
bestWeight = 0
bestTime = 0
bestQuality = 0

while i <= number:
    weight = int(input())
    time = int(input())
    quality = int(input())

    value = (weight // time) ** quality

    if value > highestValue:
        highestValue = value

        bestWeight = weight
        bestTime = time
        bestQuality = quality

    i+=1

print(f"{bestWeight} : {bestTime} = {highestValue} ({bestQuality})")

