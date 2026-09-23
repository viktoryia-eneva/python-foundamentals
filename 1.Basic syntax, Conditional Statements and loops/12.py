divisor = int(input())
boundary = int(input())

largest = 0;

for i in range(divisor, boundary + 1, 1):
    if i > 0 and i % divisor == 0 and i <= boundary:
      largest = i;

print(largest);
