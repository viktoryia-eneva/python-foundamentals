text = input()
need = 0

while(text != "END"):
    if text == "coding" or text == "dog" or text == "cat" or text == "movie":
        need+=1
    elif text == "CODING" or text == "DOG" or text == "CAT" or text == "MOVIE":
        need+=2

    text = input()

if need > 5:
    print("You need extra sleep")
else:
    print(need)