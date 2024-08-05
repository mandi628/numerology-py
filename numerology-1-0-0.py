#! /usr/bin/env python

# NUMEROLOGY 1.0.0 - mandi628
# Started 2024.08.04

letters = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":1, "K":2, "L":3, "M":4, "N":5, "O":6, "P":7, "Q":8, "R":9, "S":1, "T":2, "U":3, "V":4, "W":5, "X":6, "Y":7, "Z":8}

print("WELCOME to Numerology 1.0.0!\nNumerology calculations can be frustrating to calculate, so let me help you.")
print("\nHere are the calculations we can make:\n     1) Universal Year (current year)\n     2) Universal Month (current date)\n     3) Birth Number (birthdate)\n     4) Personal Year (current date & birthdate)\n     5) Personal Month (current date & birthdate)\n     6) Soul Number (coming soon)\n     7) Life Path Number (coming soon)\n     8) Destiny Number (coming soon)\n     9) Maturity Number (coming soon)\n    10) Other Number (coming soon)\n    11) Pinnacles & Challenges\n    12) Major Cycles\n    13) Age Vibration")
action = input("\nWhat would you like to calculate today? ")

def univ_year(year):
    year = " ".join(yr)
    yr_int = []
    for y in year.split():
       yr_int.append(int(y))
    yr_sum = sum(yr_int)
    if yr_sum > 9:
        sum_str = str(yr_sum)
        sum_string = " ".join(sum_str)
        yr_sum_int = []
        for x in sum_string.split():
            yr_sum_int.append(int(x))
        yr_sum_sum = sum(yr_sum_int)
        return yr_sum_sum
    else:
        return yr_sum

def month(mth):
    mo_no = int(mot)
    if mo_no > 9:
        mo_str = str(mo_no)
        month = " ".join(mo_str)
        mo_int = []
        for m in month.split():
            mo_int.append(int(m))
        mo_sum = sum(mo_int)
        return mo_sum
    else:
        return mo_no

def univ_month(year, mth):
    year = univ_year(yr)
    mth = month(mot)
    u_mo = year + mth
    if u_mo > 9:
        u_mo_no = str(u_mo)
        un_mo = " ".join(u_mo_no)
        umo_int = []
        for u in un_mo.split():
            umo_int.append(int(u))
        umo_sum = sum(umo_int)
        return umo_sum
    else:
        return u_mo

def pers_year(date):
    date = " ".join(bd)
    dt_int = []
    for d in date.split():
       dt_int.append(int(d))
    dt_sum = sum(dt_int)
    if dt_sum > 9:
        dt_str = str(dt_sum)
        dt_string = " ".join(dt_str)
        dt_sum_int = []
        for t in dt_string.split():
            dt_sum_int.append(int(t))
        dt_sum_sum = sum(dt_sum_int)
        return dt_sum_sum
    else:
        return dt_sum

def pers_mo(pers_year, mth):
    year = pers_year(bd)
    month = month(mot)
    p_mo = year + month
    if p_mo > 9:
        p_mo_no = str(p_mo)
        pr_mo = " ".join(p_mo_no)
        prm_int = []
        for p in pr_mo.split():
            prm_int.append(int(p))
        prm_sum = sum(prm_int)
        return prm_sum
    else:
        return p_mo

if action == "1":
    yr = input("What is the current year? ")
    univ_yr = univ_year(yr)
    print("The current Universal Year is", univ_yr)
elif action == "2":
    mot = input("What is the current month? (please enter digits) ")
    yr = input("What is the current year? ")
    univ_mo = univ_month(yr, mot)
    print("The current Universal Month is", univ_mo)
elif action == "4":
    bd = input("Please enter your birthday with the current year: (YYYYMMDD) ")
    p_yr = pers_year(bd)
    print("Your current personal year is", p_yr)
elif action == "5":
    bd = input("Please enter your birthday with the current year: (YYYYMMDD) ")
    mot = input("What is the current month? (please enter digits) ")
    p_yr = pers_year(bd)
    print("Your current personal year is", p_yr)
    print(month(mot))
    print(type(month(mot)))
    p_mo = pers_mo(bd, mot)
    print("Your current personal month is", p_mo)
else:
    print("I am not able to do that right now. Please try again later.")
