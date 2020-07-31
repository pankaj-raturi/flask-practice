##!/usr/bin/env python3

def separator():
    print("============================")

def multiply(*arguments):
    container = 1
    for value in arguments:
        container *= value
    return container

print(multiply(2,3,4))


###########################
# Unpack named arguments
###########################

def printAge(name, age):
    print(f"{name}, is {age} years old")

person = {"name":"Pankaj", "age":"30"}

printAge(**person)

separator()

#sample 2

def printAge2(**args):
    print(args)

printAge2(**person)

separator()

# Test comprehension in loops
list = {1:'a',2:'b',3:'c'}

for item in list.items():
    print(item)