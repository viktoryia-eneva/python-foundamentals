tail = input()
body = input()
head = input()

newList = [tail, body, head]

newList[0], newList[2] = newList[2], newList[0]
print(newList)
