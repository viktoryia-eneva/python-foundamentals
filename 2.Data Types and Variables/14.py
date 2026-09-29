groupSize = int(input())
days = int(input())

i = 1
coins = 0

while i <= days:
     coins += 50
     coins -= groupSize * 2

     if i % 3 == 0:
         coins -= 3 * groupSize

     if i % 5 == 0:
         coins += 20 * groupSize
         if i % 3 == 0:
          coins -= 2 * groupSize

     if i % 10 == 0:
         groupSize -= 2

     if i % 15 == 0:
         groupSize += 5
          
     i += 1

coins_each = coins // groupSize

print(f"{groupSize} companions received {coins_each} coins each.")
