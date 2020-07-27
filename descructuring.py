#!/usr/bin/env python3

friends = [('Pankaj', 29, 'Software Engineer'), ('Jetinder', '24', 'Mechanical Enginerr')]

for counter, (name, age, profession) in enumerate(friends):
    print(f"Counter: {counter}, Name: {name}, Age: {age} years, Profession: {profession}")
    print()