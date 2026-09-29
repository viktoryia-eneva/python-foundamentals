year = int(input())
findHappyYear = False

while not findHappyYear:
    year += 1

    digit1 = year % 10
    digit2 = int(year / 10) % 10
    digit3 = int(year / 100) % 10
    digit4 = int(year / 1000) % 10

    if digit1 != digit2 and digit1 != digit3 and digit1 != digit4 \
     and digit2 != digit3 and digit2 != digit4 \
     and digit3 != digit4:

     findHappyYear = True

print(year)