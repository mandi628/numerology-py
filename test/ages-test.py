#! /usr/bin/env python

def make_list(entry):
    ent_list = " ".join(entry)
    ent_int = []
    for e in ent_list.split():
        ent_int.append(int(e))
    return ent_int

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

def lp_no(birth):
    birth_list = make_list(birth)
    lpath = simplify(birth_list)
    return lpath

def ages(birth):
    lpn = lp_no(birth)
    ages = []
    if lpn == 1:
        ages.append(26)
        ages.append(53)
    elif lpn == 2:
        ages.append(25)
        ages.append(52)
    elif lpn == 3:
        ages.append(33)
        ages.append(60)
    elif lpn == 4:
        ages.append(32)
        ages.append(59)
    elif lpn == 5:
        ages.append(31)
        ages.append(58)
    elif lpn == 6:
        ages.append(30)
        ages.append(57)
    elif lpn == 7:
        ages.append(29)
        ages.append(56)
    elif lpn == 8:
        ages.append(28)
        ages.append(55)
    else:
        ages.append(27)
        ages.append(54)
    return ages

birth = input("Enter a birthday ")

cycle_ages = ages(birth)
print(cycle_ages)
