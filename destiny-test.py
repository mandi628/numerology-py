#! /usr/bin/env python

letters = {
    "A":1,
    "B":2,
    "C":3,
    "D":4,
    "E":5,
    "F":6,
    "G":7,
    "H":8,
    "I":9,
    "J":1,
    "K":2,
    "L":3,
    "M":4,
    "N":5,
    "O":6,
    "P":7,
    "Q":8,
    "R":9,
    "S":1,
    "T":2,
    "U":3,
    "V":4,
    "W":5,
    "X":6,
    "Y":7,
    "Z":8
}

first = input("Enter your first name: ")
first = first.upper()
first_sp = " ".join(first)
print(first_sp)
first_list = []
for f in first_sp.split():
    first_list.append(f)
print(first_list)
first_int = []
for i in first_list:
    first_int.append(letters.get(i))
print(first_int)
