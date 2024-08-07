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
    print("\nPredictive Calculations:\n     i) Personal Year\n     j) Personal Month\n     k) Personal Day\n     l) Pinnacles & Challenges\n     m) Major Cycles\n     n) Age Vibration")
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

def birth_s(birth):
    birth_s = []
    day = simplify(make_list(birth[3:5]))
    birth_s.append(day)
    mon = simplify(make_list(birth[:2]))
    birth_s.append(mon)
    by = simplify(make_list(birth[6:]))
    birth_s.append(by)
    return birth_s

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
    mc1 = simplify(make_list(str(birth_s(birth)[1])))
    cycles.append(mc1s)
    mc2 = simplify(make_list(str(birth_s(birth)[0])))
    cycles.append(mc2s)
    mc3 = simplify(make_list(str(birth_s(birth)[2])))
    cycles.append(mc3s)
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
        print("Their second Major Cycle, from age %d to %d, is a %d." % (first, (ages[0] + 1), ages[1], major_cycles[1]))
        print("And their third Major Cycle, from age %d to death, is a %d." % (first, (ages[1] + 1), major_cycles[2]))

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
