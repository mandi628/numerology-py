#! usr/bin/env python

from calcs.simplify import *
from calcs.list import *
from calcs.strings import *
from calcs.core import *
from datetime import datetime
from datetime import date

def univ_yr(now):
    univ_yr = simplify(make_list(date_s(now)[:4]))
    return univ_yr

def univ_mo(now):
    mo = simplify(make_list(date_s(now)[5:7]))
    univ_mo = simplify(make_list(str(univ_yr(now) + mo)))
    return univ_mo

def pers_yr(birth, now):
    pers_yr = simplify(make_list(str(birth_s(birth)[0] + birth_s(birth)[1] + date_s(now)[2])))
    return pers_yr

def pers_mo(birth, now):
    pers_mo = simplify(make_list(str(pers_yr(birth, now) + date_s(now)[1])))
    return pers_mo

def pers_day(birth, now):
    pers_day = simplify(make_list(str(pers_mo(birth, now) + date_s(now)[0])))
    return pers_day

def calculateAge(birth):
    birthDate = datetime.strptime(birth, "%m %d %Y")
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

def age_vib(birth):
    age = calculateAge(birth)
    age1 = age + 1
    age_vib = simplify(make_list(str(age + age1)))
    return age_vib

def maj_cycles(birth):
    cycles = []
    mc1 = simplify(make_list(str(birth_s(birth)[1])))
    cycles.append(mc1)
    mc2 = simplify(make_list(str(birth_s(birth)[0])))
    cycles.append(mc2)
    mc3 = simplify(make_list(str(birth_s(birth)[2])))
    cycles.append(mc3)
    return cycles

def cycle_age(birth):
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
