#! /usr/bin/env python

# NUMEROLOGY 0.6.2 - mandi628
# Started 2024.08.06; updated 2025.02.16

from datetime import datetime
from datetime import date

from calcs.menu import *
from calcs.list import *
from calcs.simplify import *
from calcs.core import *
from calcs.predictions import *
from calcs.strings import *

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
nick = input("Does this person have a nickname? y/n ")

def nickName():
    if nick == "y":
        nickName = input("What is the person's nickname? ")
        return nickName
    else:
        return
nickName()
birth = input("What is the person's birthdate? (MM DD YYYY) ")
now = datetime.today()

menu()
#data()
again = "y"

while again == "y":
    action = input("\n:: ")
    if action == "a": # Universal Year
        univyr = date_s(now)[2]
        print("The current Universal Year is", univyr)

    elif action == "b": # Universal Month
        univmo = simplify(make_list(str(date_s(now)[2] + date_s(now)[1])))
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
        persyr = pers_yr(birth, now)
        print("%s's Personal Year number is %d." % (first, persyr))

    elif action == "j": # Personal Month
        persmo = pers_mo(birth, now)
        print("%s's Personal Month number is %d." % (first, persmo))
        file_path = 'def/pm/%s.txt' % persmo
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                print(file_content)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif action == "k": # Personal Day
        persday = pers_day(birth, now)
        print("%s's Personal Day number is %d." % (first, persday))
        file_path = 'def/pd/%s.txt' % persday
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                print(file_content)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

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
        file_path = 'def/mc/%s.txt' % major_cycles[0]
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                print(file_content)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        print("Their second Major Cycle, from age %d to %d, is a %d." % ((ages[0] + 1), ages[1], major_cycles[1]))
        file_path = 'def/mc/%s.txt' % major_cycles[1]
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                print(file_content)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")
        print("And their third Major Cycle, from age %d to death, is a %d." % ((ages[1] + 1), major_cycles[2]))
        file_path = 'def/mc/%s.txt' % major_cycles[2]
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                print(file_content)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif action == "n": # Age Vibration
        agevibe = age_vib(birth)
        print("%s's Age Vibration this year is %d." % (first, agevibe))
        file_path = 'def/av/%s.txt' % agevibe
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                print(file_content)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif action == "menu":
        menu()

    elif action == "exit":
        break

    elif action == "help":
        file_path = 'help.txt'
        try:
            with open(file_path, 'r') as file:
                file_content = file.read()
                print("Help - Numerology 0.6.2\n", file_content)
        except FileNotFoundError:
            print(f"File '{file_path}' not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    elif action == "new":
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
        nick = input("Does this person have a nickname? y/n ")

        def nickName():
            if nick == "y":
                nickName = input("What is the person's nickname? ")
                return nickName
            else:
                return
        nickName()
        birth = input("What is the person's birthdate? (MM DD YYYY) ")
        now = datetime.today()

    else:
        print("I'm sorry that's not a valid option.")
#    again = input("\nWould you like to calculate something else? (y/n) ")
print("\nThank you for trying Numerology! Have a great day! :)\n")
