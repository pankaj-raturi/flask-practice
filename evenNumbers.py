#!/usr/bin/env python3

def separator():
    print("================================")


# Even numbes Up to 20

#Print all even Numbers
for number in range(1, 21):
    if number % 2 == 0:
        print(number)

separator()

#Even numbers By range
for number in range(0, 21, 2):
    print(number)


separator()

#by List comprehension
evenNumbers = [number for number in range(1, 20) if number %2 == 0 ]

print(evenNumbers)