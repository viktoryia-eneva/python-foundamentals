decQuantity = int(input())
daysLeft = int(input())

totalCost = 0
spirit = 0

for day in range(1, daysLeft + 1):

    if day % 11 == 0:
        decQuantity +=2

    if day % 2 == 0:
        totalCost + decQuantity * 2
        spirit += 5

    if day % 3 == 0:
        totalCost += decQuantity * 5
        totalCost += decQuantity * 3
        spirit +=3
        spirit +=10

    if day % 5 == 0:
        totalCost += decQuantity * 15
        spirit += 17

    if day % 3 == 0 and day % 5 == 0:
        spirit += 30

    if day % 10 == 0:
        spirit -= 20
        totalCost += 5 + 3 + 15

if daysLeft % 10 == 0:
    spirit -= 30

print(f"Total cost: {totalCost}")
print(f"Total spirit: {spirit}")