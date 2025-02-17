#! usr/bin/env python

from calcs.simplify import *
from calcs.list import *

def lp_no(birth):
    lpath = simplify(make_list(birth))
    return lpath

def soul_no(first, middle, last):
    name_s = first + middle + last
    soul = simplify(not_cons(name_s))
    return soul

def dest_no(first, middle, last):
    name_d = first + middle + last
    destiny = simplify((convert(name_d)))
    return destiny

def maturity(birth, first, middle, last):
    mat_no = simplify(make_list(str(lp_no(birth) + dest_no(first, middle, last))))
    return mat_no

def personality(first, middle, last):
    name_p = first + middle + last
    pers = simplify(consonants(name_p))
    return pers

