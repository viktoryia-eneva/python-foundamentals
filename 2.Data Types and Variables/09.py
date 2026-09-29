import math

numberPeople = int(input())
capacity = int(input())

fullCourses = int(numberPeople / capacity)

if numberPeople % capacity != 0:
    fullCourses+=1

print(fullCourses)