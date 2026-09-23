ordersCount = int(input())

price = 0;
total = 0;

for i in range(ordersCount):
    pricePerCapsule = float(input())
    days = int(input())
    capsulesPerDay = int(input())

    if pricePerCapsule < 0.01 or pricePerCapsule > 100:
        continue

    if days < 1 or days > 31:
        continue

    if capsulesPerDay < 1 or capsulesPerDay > 2000:
        continue

    price = pricePerCapsule * days * capsulesPerDay
    total+=price

    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total:.2f}")