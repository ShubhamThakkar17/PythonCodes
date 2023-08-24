import sys
date = input("Date: ") #yyyy-month-dd
y, m, d = date.split("-")
y = int(y)
m = int(m)
d = int(d)

#year validation
if y<0 or y>2023:
    sys.exit("Invalid")
if m<1 or m>12:
    sys.exit("Invalid")
if d<1 or d>31:
    sys.exit("invalid")
elif m ==2 and d<1 or d>29:
    sys.exit("Invalid")
