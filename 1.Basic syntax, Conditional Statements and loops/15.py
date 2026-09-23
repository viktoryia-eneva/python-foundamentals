text = input()

while(text != "End"):
    if text == "SoftUni":
        text = input()
        continue

    index = ""

    for i in range(len(text)):
       index +=text[i] * 2
    
    print(index)

    text = input()