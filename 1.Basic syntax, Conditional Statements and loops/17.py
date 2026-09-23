text = input()
new = input()

index = ""

for i in range(len(text)):
       if text[i] != new[i]:
        text = text[:i] + new[i] + text[i + 1:]
        print(text)       

