budget = float(input())
pricePer1Kg = float(input())

numberLoaf = 0
colouredEggs = 0

price1kgEggs = 0.75 * pricePer1Kg
price1LMilk = 0.25 * pricePer1Kg + pricePer1Kg
neededMilk = price1LMilk / 4

pricePerLoaf = pricePer1Kg + price1kgEggs + neededMilk

while budget >= pricePerLoaf:
      budget-=pricePerLoaf

      numberLoaf+=1
      colouredEggs+=3

      if numberLoaf % 3 == 0:
            colouredEggs -= numberLoaf - 2

print(f"You made {numberLoaf} loaves of Easter bread! "
    f"Now you have {colouredEggs} eggs and {budget:.2f}BGN left.")