#! usr/bin/env python

from calcs.simplify import *
from calcs.list import *

def date_s(now):
    date_str = now.strftime("%Y %m %d")
    date_s = []
    date_d = simplify(make_list(date_str[8:]))
    date_s.append(date_d)
    date_m = simplify(make_list(date_str[5:7]))
    date_s.append(date_m)
    date_y = simplify(make_list(date_str[:4]))
    date_s.append(date_y)
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

