#! /usr/bin/env python

# NUMEROLOGY 0.6.2 - mandi628
# Started 2024.08.06; updated 2025.02.16

from datetime import datetime
from datetime import date

from calcs.menu import *
from calcs.list import *
from calcs.simplify import *
from calcs.core import *

print("\nWELCOME to Numerology 0.6.2!\nNumerology calculations can be frustrating to calculate, so let me help you.")
print("\nTo use this app, type the number of the calculation you would like to calculate.")
print("'menu' - Display the menu options again.")
print("'new' - Asks for new subject data.")
print("'help' - Displays the help file.")
print("'exit' - Exits the program.")

first = input("\nWhat is the person's full first name? ")
middle = input("What is the person's middle name? ")
last = input("What is the person's last name at birth? ")
female = input("Does this person have a married name? y/n ")

def married():
    if female == "y":
        married = input("What is the person's married name? ")
        return married
    else:
        return
married()
birth = input("What is the person's birthdate? (MM DD YYYY) ")

def date_s(date):
    date_s = []
    day_d = simplify(make_list(date[3:5]))
    date_s.append(day_d)
    mon_d = simplify(make_list(date[:2]))
    date_s.append(mon_d)
    dy = simplify(make_list(date[6:]))
    date_s.append(dy)
    return date_s

def birth_s(birth):
    birth_s = []
    day = simplify(make_list(birth[3:5]))
    birth_s.append(day)
    mon = simplify(make_list(birth[:2]))
    birth_s.append(mon)
    by = simplify(make_list(birth[6:]))
    birth_s.append(by)
    return birth_s

def univ_yr(date):
    univ_yr = simplify(make_list(str(date_s(date)[2])))
    return univ_yr

def pers_yr(birth, date):
    pers_yr = simplify(make_list(str(birth_s(birth)[0] + birth_s(birth)[1] + date_s(date)[2])))
    return pers_yr

def univ_mo(date):
    univ_mo = simplify(make_list(str(date_s(date)[1] + date_s(date)[2])))
    return univ_mo

def pers_mo(birth, date):
    pers_mo = simplify(make_list(str(pers_yr(birth, date) + date_s(date)[1])))
    return pers_mo

def pers_day(birth, date):
    pers_day = simplify(make_list(str(pers_mo(birth, date) + date_s(date)[0])))
    return pers_day

def calculateAge(birth):
    birthDate = datetime.strptime(birth, "%m %d %Y")
    today = date.today()
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    return age

def age_vib():
    calculateAge(birth)
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

menu()
#data()
again = "y"

while again == "y":
    action = input("\n:: ")
    if action == "a": # Universal Year
        univyr = univ_yr(date)
        print("The current Universal Year is", univyr)

    elif action == "b": # Universal Month
        univmo = univ_mo(date)
        print("The current Universal Month is", univmo)

    elif action == "c": # Birth Number
        print("\nThis is the numerological significance of the day of the month they were born on.")
        b_no = birth_s(birth)[0]
        print("%s's Birth Number is %d." % (first, b_no))

    elif action == "d": # Soul Number
        soul = soul_no(first, middle, last)
        print("%s's Soul Number is %d." % (first, soul))

    elif action == "e": # Life Path Number
        l_path = lp_no(birth)
        print("%s's Life Path Number is %d." % (first, l_path))

    elif action == "f": # Destiny Number
        destiny = dest_no(first, middle, last)
        print("%s's Destiny Number is %d." % (first, destiny))

    elif action == "g": # Maturity Number
        matur_no = maturity(birth, first, middle, last)
        print("%s's Maturity Number is %d." % (first, matur_no))

    elif action == "h": # Personality Number
        pers_no = personality(first, middle, last)
        print("%s's Personality Number is %d." % (first, pers_no))

    elif action == "i": # Personal Year
        persyr = pers_yr(birth, date)
        print("%s's Personal Year number is %d." % (first, persyr))

    elif action == "j": # Personal Month
        persmo = pers_mo(birth, date)
        print("%s's Personal Month number is %d." % (first, persmo))

    elif action == "k": # Personal Day
        persday = pers_day(birth, date)
        print("%s's Personal Day number is %d." % (first, persday))

    elif action == "l": # Pinnacles & Challenges
        pinns = pinnacles(birth)
        chall = challenges(birth)
        pin_age = pin_ages(birth)
        print("\nThe Pinnacle Numbers show your potential successes during different periods in your life.")
        print("Your Challenge Numbers let you know your potential difficulties during those periods.\n")
        print("%s's First Pinnacle, from birth to age %d, is a %d. During that time, they'll face a Challenge Number %d." % (first, pin_age[0], pinns[0], chall[0]))
        print("Their Second Pinnacle is %d, from age %d to %d, with a Challenge of %d." % (pinns[1], pin_age[0], pin_age[1], chall[1]))
        print("During the Third Pinnacle, ages %d to %d, they'll face a Pinnacle Number %d and a Challenge Number %d." % (pin_age[1], pin_age[2], pinns[2], chall[2]))
        print("And in the last Pinnacle, Pinnacle Number %d and Challenge Number %d with take them from age %d to the end of their life." % (pinns[3], chall[3], pin_age[2]))

    elif action == "m": # Major Cycles
        major_cycles = maj_cycles(birth)
        ages = cycle_age(birth)
        print("%s's first Major Cycle, from birth to age %d, is a %d." % (first, ages[0], major_cycles[0]))
        print("Their second Major Cycle, from age %d to %d, is a %d." % ((ages[0] + 1), ages[1], major_cycles[1]))
        print("And their third Major Cycle, from age %d to death, is a %d." % ((ages[1] + 1), major_cycles[2]))

    elif action == "n": # Age Vibration
        agevibe = age_vib()
        print("%s's Age Vibration this year is %d." % (first, agevibe))

    elif action == "menu":
        menu()

    elif action == "exit":
        break

    elif action == "help":
        file_path = 'help.txt'
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                print("Help - Numerology 0.2.0\n", file_content)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif action == "new":
        first = input("\nWhat is the person's full first name? ")
        middle = input("What is the person's middle name? ")
        last = input("What is the person's last name at birth? ")
        birth = input("What is the person's birthdate? (MM DD YYYY) ")
        date = input("What is the current date? (MM DD YYYY) ")

    else:
        print("I'm sorry that's not a valid option.")
#    again = input("\nWould you like to calculate something else? (y/n) ")
print("\nThank you for trying Numerology! Have a great day! :)\n")
