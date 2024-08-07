#! /usr/bin/env python

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

def make_list(entry):
    ent_list = " ".join(entry)
    ent_int = []
    for e in ent_list.split():
        ent_int.append(int(e))
    return ent_int


birth = "06 28 1976"

cycles = []
mc1 = birth[:2]
mc1_list = make_list(mc1)
mc1s = simplify(mc1_list)
cycles.append(mc1s)

mc2 = birth[3:5]
mc2_list = make_list(mc2)
mc2s = simplify(mc2_list)
cycles.append(mc2s)

mc3 = birth[6:]
mc3_list = make_list(mc3)
mc3s = simplify(mc3_list)
cycles.append(mc3s)

print(cycles)
