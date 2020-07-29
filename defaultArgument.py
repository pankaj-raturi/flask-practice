#!/usr/bin/env python3

default = 8


def add(a, b=default):
    print(f"Sum: {a+b}")


add(5)
add(5,6)