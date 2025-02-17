#! usr/bin/env python

letters = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":1, "K":2, "L":3, "M":4, "N":5, "O":6, "P":7, "Q":8, "R":9, "S":1, "T":2, "U":3, "V":4, "W":5, "X":6, "Y":7, "Z":8}

vowels = ["A", "E", "I", "O", "U", "Y"]


def simplify(ent_int):
    num_sum = sum(ent_int)
    if num_sum > 9:
        sum_str = str(num_sum)
        sum_string = " ".join(sum_str)
        num_sum_int = []
        for s in sum_string.split():
            num_sum_int.append(int(s))
        num_ss = sum(num_sum_int)
        if num_ss > 9:
            num_ss_str = str(num_ss)
            num_string = " ".join(num_ss_str)
            num_ss_int = []
            for i in num_string.split():
                num_ss_int.append(int(i))
            num_sss = sum(num_ss_int)
            return num_sss
        else:
            return num_ss
    else:
        return num_sum

def convert(name):
    name = name.upper()
    name_sp = " ".join(name)
    name_list = []
    for n in name_sp.split():
        name_list.append(n)
    name_int = []
    for n in name_list:
        name_int.append(letters.get(n))
    return name_int

def consonants(name):
    nameu = name.upper()
    name_sp = " ".join(nameu)
    name_list = []
    for n in name_sp.split():
        if n not in vowels:
            name_list.append(n)
    con_int = []
    for i in name_list:
        con_int.append(letters.get(i))
    return con_int

def not_cons(name):
    nameup = name.upper()
    name_sp = " ".join(nameup)
    name_list = []
    for n in name_sp.split():
        if n in vowels:
            name_list.append(n)
    vow_int = []
    for i in name_list:
        vow_int.append(letters.get(i))
    return vow_int

