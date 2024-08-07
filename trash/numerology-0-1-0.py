#! /usr/bin/env python

# NUMEROLOGY 1.0.0 - mandi628
# Started 2024.08.04

#letters = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":1, "K":2, "L":3, "M":4, "N":5, "O":6, "P":7, "Q":8, "R":9, "S":1, "T":2, "U":3, "V":4, "W":5, "X":6, "Y":7, "Z":8}

print("WELCOME to Numerology 1.0.0!\nNumerology calculations can be frustrating to calculate, so let me help you.")
print("\nHere are the calculations we can make:")
print("\nUniversal Numbers:\n     1) Universal Year\n     2) Universal Month")
print("\nBasic Calculations:\n     3) Birth Number")
# 4) Soul Number (coming soon)\n     5) Life Path Number (coming soon)\n     6) Destiny Number (coming soon)\n     7) Maturity Number (coming soon)\n     8) Other Number (coming soon)
print("\nPredictive Calculations:\n     9) Personal Year\n    10) Personal Month\n    11) Personal Day\n    14) Age Vibration")
#12) Pinnacles & Challenges\n    13) Major Cycles\n
"""print("\nComplete Charts:\n    15) Birth Chart (w/option to save)\n    16) Comparison Chart (w/option to save)\n    17) Prediction Chart (w/option to save)")"""

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

again = "y"

while again == "y":
    action = input("\nWhat would you like to calculate today? ")
    name = input("\nWhat is the person's name? ")
    if action == "1":
        yr = input("What is the current year? ")
        yr_list = make_list(yr)
        univ_yr = simplify(yr_list)
        print("The current Universal Year is", univ_yr)

    elif action == "2":
        mot = input("What is the current month? (please enter digits) ")
        yr = input("What is the current year? ")
        mot_list = make_list(mot)
        yr_list = make_list(yr)
        um_list = mot_list + yr_list
        univ_mo = simplify(um_list)
        print("The current Universal Month is", univ_mo)

    elif action == "3":
        print("\nThis is the numerological significance of the day of the month they were born on.")
        date = input("What the day number of birth? ")
        date_list = make_list(date)
        b_no = simplify(date_list)
        print("%s's Birth Number is %d." % (name, b_no))

    elif action == "4":
        print("I'm sorry - I can't do that yet.")

    elif action == "5":
        print("I'm sorry - I can't do that yet.")

    elif action == "6":
        print("I'm sorry - I can't do that yet.")

    elif action == "7":
        print("I'm sorry - I can't do that yet.")

    elif action == "8":
        print("I'm sorry - I can't do that yet.")

    elif action == "9":
        bd = input("What is the birth month and day (MMDD)? ")
        yr = input("What is the current year (YYYY)? ")
        bd_list = make_list(bd)
        yr_list = make_list(yr)
        py_list = bd_list + yr_list
        pers_yr = simplify(py_list)
        print("%s's Personal Year number is %d." % (name, pers_yr))

    elif action == "10":
        bd = input("What is the birth month and day (MMDD)? ")
        mo = input("What is the current year & month (MMYYYY)? ")
        bd_list = make_list(bd)
        mo_list = make_list(mo)
        pm_list = bd_list + mo_list
        pers_mo = simplify(pm_list)
        print("%s's Personal Month number is %d." % (name, pers_mo))

    elif action == "11":
        bd = input("What is the birth month and day (MMDD)? ")
        day = input("What is the current date? (MMDDYYYY)? ")
        bd_list = make_list(bd)
        print(bd_list)
        day_list = make_list(day)
        print(day_list)
        pd_list = bd_list + day_list
        print(pd_list)
        pers_day = simplify(pd_list)
        print("%s's Personal Day number is %d." % (name, pers_day))

    else:
        print("I am not able to do that right now. Please try again later.")
    again = input("\nWould you like to calculate something else? (y/n) ")
print("\nThank you for trying Numerology! Have a great day! :)\n")
