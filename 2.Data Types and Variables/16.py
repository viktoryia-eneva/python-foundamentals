count = int(input())
helmetPrice = float(input())
swordPrice = float(input())
shieldPrice = float(input())
armorPrice = float(input())

i = 1
hBroken = 0
sBroken = 0
shBroken = 0
arBroken = 0

while i <= count:
    if i % 2 == 0:
      hBroken += 1

    if i % 3 == 0:
       sBroken += 1

    if i % 2 == 0 and i % 3 == 0:
       shBroken += 1

       if shBroken % 2 == 0:
         arBroken += 1

    i += 1

helExpenses = hBroken * helmetPrice
swoExpenses = sBroken * swordPrice
shieldExpenses = shBroken * shieldPrice
armExpenses = arBroken * armorPrice


total = helExpenses + swoExpenses + shieldExpenses + armExpenses

print(f"Gladiator expenses: {total:.2f} aureus")
    