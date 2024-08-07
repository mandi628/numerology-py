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

def birth_s(birth):
    birth_s = []
    day = simplify(make_list(birth[3:5]))
    birth_s.append(day)
    mon = simplify(make_list(birth[:2]))
    birth_s.append(mon)
    by = simplify(make_list(birth[6:]))
    birth_s.append(by)
    return birth_s

def cycles(birth):
    cycles = []
    mc1 = simplify(make_list(str(birth_s(birth)[1])))
    cycles.append(mc1)

    mc2 = simplify(make_list(str(birth_s(birth)[0])))
    cycles.append(mc2)

    mc3 = simplify(make_list(str(birth_s(birth)[2])))
    cycles.append(mc3)
    return cycles

def pinnacles(birth):
    pinnacles = []

    pn1 = simplify(make_list(str(birth_s(birth)[0] + birth_s(birth)[1])))
    pinnacles.append(pn1)
    pn2 = simplify(make_list(str(birth_s(birth)[0] + birth_s(birth)[2])))
    pinnacles.append(pn2)
    pn3 = simplify(make_list(str(pn1 + pn2)))
    pinnacles.append(pn3)
    pn4 = simplify(make_list(str(birth_s(birth)[1] + birth_s(birth)[2])))
    pinnacles.append(pn4)
    return pinnacles

def challenges(birth):
    challenges = []

    ch1 = simplify(make_list(str(abs(birth_s(birth)[0] - birth_s(birth)[1]))))
    challenges.append(ch1)
    ch2 = simplify(make_list(str(abs(birth_s(birth)[0] - birth_s(birth)[2]))))
    challenges.append(ch2)
    ch3 = simplify(make_list(str(abs(ch1 - ch2))))
    challenges.append(ch3)
    ch4 = simplify(make_list(str(abs(birth_s(birth)[1] - birth_s(birth)[2]))))
    challenges.append(ch4)
    return challenges

def lp_no(birth):
    lpath = simplify(make_list(birth))
    return lpath

def pin_ages(birth):
    lfpn = lp_no(birth)
    p_ages = []
    age1 = 36 - lfpn
    p_ages.append(age1)
    age2 = age1 + 9
    p_ages.append(age2)
    age3 = age2 + 9
    p_ages.append(age3)
    return p_ages

birth = "06 28 1976"
print("Birth: ", birth)

life_path = lp_no(birth)
print("Life Path: ", life_path)
maj_cycles = cycles(birth)
print("Major cyles: ", maj_cycles)

pinn = pinnacles(birth)
print("Pinnacles: ", pinn)

chal = challenges(birth)
print("Challenges: ", chal)

pinn_ages = pin_ages(birth)
print("Pinnacle Ages: ", pinn_ages)
