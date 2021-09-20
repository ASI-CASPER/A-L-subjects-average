def average (x,y,z) :
    qq = (x+y+z)
    avg = qq // 3
    return avg


q = float(input("marks of first subjects :-"))
w = float(input ("marks of second subjects :-"))
e = float(input ("marks of therid subjects :-"))
a = average (q,w,e)
print(("your average :-"),( float (a)))