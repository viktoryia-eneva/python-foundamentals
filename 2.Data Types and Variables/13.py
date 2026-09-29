n = int(input())

CAPACITY = 255
i = 1
sum = 0

while i <= n:
    liters = int(input())
 
    if sum + liters > CAPACITY:
      print("Insufficient capacity!")
    else:
      sum += liters

    i+=1
     
print(sum) 