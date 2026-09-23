n = int(input())

for i in range(n):
    number = int(input())
    if not number % 2 == 0:
        print(f"{number} iss odd!")
        break
else:
        print("All numbers are even.")
