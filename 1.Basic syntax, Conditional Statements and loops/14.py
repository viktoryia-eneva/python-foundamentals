number = int(input())

for i in range(number):
    text = input()

    for j in range(len(text)):
     if text[j] == "," or text[j] == "." or text[j] =="_":
        print(f"{text} is not pure.")
        break
     
    else:
        print(f"{text} is pure!")