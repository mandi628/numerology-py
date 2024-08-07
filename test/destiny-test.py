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

vowels = ["A", "E", "I", "O", "U", "Y"]

first = "Amanda"
middle = "Christine"
last = "Saidat"

name = first + middle + last
print(name)
name = name.upper()
print(name)
name_sp = " ".join(name)
print(name_sp)
name_list = []
for n in name_sp.split():
    if n in vowels:
        name_list.append(n)
print(name_list)
name_int = []
for i in name_list:
    name_int.append(letters.get(i))
print(name_int)
