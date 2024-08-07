#! /usr/bin/env python

# NUMEROLOGY 0.2.0 - mandi628
# Started 2024.08.06

letters = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I":9, "J":1, "K":2, "L":3, "M":4, "N":5, "O":6, "P":7, "Q":8, "R":9, "S":1, "T":2, "U":3, "V":4, "W":5, "X":6, "Y":7, "Z":8}

vowels = ["A", "E", "I", "O", "U", "Y"]

print("\nWELCOME to Numerology 0.2.0!\nNumerology calculations can be frustrating to calculate, so let me help you.")
print("\nTo use this app, type the number of the calculation you would like to calculate.")
print("'menu' - Display the menu options again.")
print("'new' - Asks for new subject data.")
print("'help' - Displays the help file.")
print("'exit' - Exits the program.")

def menu():
    print("\nHere are the calculations we can make:")
    print("\nUniversal Numbers:\n     a) Universal Year\n     b) Universal Month")
    print("\nBasic Calculations:\n     c) Birth Number\n     d) Soul Number\n     e) Life Path Number\n     f) Destiny Number\n     g) Maturity Number\n     h) Personality Number")
    print("\nPredictive Calculations:\n     i) Personal Year\n     j) Personal Month\n     k) Personal Day\n     m) Major Cycles\n     n) Age Vibration")
    # \n    12) Pinnacles & Challenges
#    print("\nComplete Charts:\n    15) Birth Chart (w/option to save)\n    16) Comparison Chart (w/option to save)\n    17) Prediction Chart (w/option to save)\n    18) Prediction Comparison Chart (w/option to save)")
    print("\nApp Options:\n     'menu' - Display the menu options again.\n     'new' - Prompts for new subject data.\n     'help' - Display help file.\n     'exit' - Exit the program.")

first = input("\nWhat is the person's full first name? ")
middle = input("What is the person's middle name? ")
last = input("What is the person's last name at birth? ")
birth = input("What is the person's birthdate? (MM DD YYYY) ")
date = input("What is the current date? (MM DD YYYY) ")

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

def lp_no(birth):
    birth_list = make_list(birth)
    lpath = simplify(birth_list)
    return lpath

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

def univ_yr(date):
    yru = date[-4:]
    yr_list = make_list(yru)
    univ_yr = simplify(yr_list)
    return univ_yr

def pers_yr(birth, date):
    birthp = birth[:5]
    datep = date[-4:]
    pyr = birth + date
    pyr_list = make_list(pyr)
    pers_yr = simplify(pyr_list)
    return pers_yr

def univ_mo(date):
    mou = date[:2] + date[-4:]
    mo_list = make_list(mou)
    univ_mo = simplify(mo_list)
    return univ_mo

def pers_mo(birth, date):
    birthpm = birth[:5]
    datepm = date[:2] + date[-4:]
    pmo = birthpm + datepm
    pmo_list = make_list(pmo)
    pers_mo = simplify(pmo_list)
    return pers_mo

def pers_day(birth, date):
    birthpd = birth[:5]
    datepd = date
    pday = birthpd + datepd
    pday_list = make_list(pday)
    pers_day = simplify(pday_list)
    return pers_day

def birth_no(birth):
    dateb = birth[3:5]
    date_list = make_list(dateb)
    b_no = simplify(date_list)
    return b_no

def soul_no(first, middle, last):
    name_s = first + middle + last
    vow = not_cons(name_s)
    soul = simplify(vow)
    return soul

def dest_no(first, middle, last):
    name_d = first + middle + last
    named_int = convert(name_d)
    destiny = simplify(named_int)
    return destiny

def maturity(birth, first, middle, last):
    birth_list = make_list(birth)
    name_m = first + middle + last
    namem_int = convert(name_m)
    mat = birth_list + namem_int
    mat_no = simplify(mat)
    return mat_no

def personality(first, middle, last):
    name_p = first + middle + last
    con = consonants(name_p)
    pers = simplify(con)
    return pers

def age_vib():
    age = int(input("What was %s's age at the beginning of the year? " % first))
    age1 = age + 1
    age_ls = str(age) + str(age1)
    age_list = make_list(age_ls)
    age_vib = simplify(age_list)
    return age_vib

def maj_cycles(birth):
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
    return cycles

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
        b_no = birth_no(birth)
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
        print("I'm sorry - I can't do that yet.")

    elif action == "m": # Major Cycles
        major_cycles = maj_cycles(birth)
        print(major_cycles)

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
