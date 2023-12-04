#   Aiden Morrison
#   CSCI 128 – Section J
#   Assessment 4
#   References: no one
#   Time: 3 Hour


# inputing 3 lines as floats and spliting into x and y
x1, y1 = map(float, input("P1> ").split())
x2, y2 = map(float, input("P2> ").split())
x3, y3 = map(float, input("P3> ").split())

# rounding the inputs and doing math shennanigans 
d1 = round(((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5, 4)
d2 = round(((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5, 4)
d3 = round(((x1 - x3) ** 2 + (y1 - y3) ** 2) ** 0.5, 4)

# sorting the sides 
sides = [d1, d2, d3]
sides.sort()

# if duplicate point, output
if (x1, y1) == (x2, y2) or (x1, y1) == (x3, y3) or (x2, y2) == (x3, y3):
    print("OUTPUT [{}]".format(', '.join([str(round(side, 4)) for side in sides])))
    print("OUTPUT Duplicate Point")
else:
    collinear = (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) == 0
    # nested if statement, checks if collinear and outputs or moves on
    if collinear:
        print("OUTPUT [{}]".format(', '.join([str(round(side, 4)) for side in sides])))
        print("OUTPUT Collinear")
        # else, checking if equilateral
    else:
        if d1 == d2 == d3:
            print("OUTPUT [{}]".format(', '.join([str(round(side, 4)) for side in sides])))
            print("OUTPUT Acute Equilateral Triangle")
            # elif, checking if acute isosceles
        elif d1 == d2 or d2 == d3 or d1 == d3:
            print("OUTPUT [{}]".format(', '.join([str(round(side, 4)) for side in sides])))
            print("OUTPUT Acute Isosceles Triangle")
            # elif, checking if obtuse isosceles
        elif d1 ** 2 + d2 ** 2 < d3 ** 2:
            if abs(d1 - d2) < 0.0001 or abs(d2 - d3) < 0.0001 or abs(d1 - d3) < 0.0001:
                print("OUTPUT [{}]".format(', '.join([str(round(side, 4)) for side in sides])))
                print("OUTPUT Obtuse Isosceles Triangle")
                # if not obtuse isosceles, obtuse scalene
            else:
                print("OUTPUT [{}]".format(', '.join([str(round(side, 4)) for side in sides])))
                print("OUTPUT Obtuse Scalene Triangle")
        # elif, checking if right scalene
        elif abs(d1 ** 2 + d2 ** 2 - d3 ** 2) < 0.0001 or abs(d2 ** 2 + d3 ** 2 - d1 ** 2) < 0.0001 or abs(d1 ** 2 + d3 ** 2 - d2 ** 2) < 0.0001:
            print("OUTPUT [{}]".format(', '.join([str(round(side, 4)) for side in sides])))
            print("OUTPUT Right Scalene Triangle")
            # else, its acute scalene
        else:
            print("OUTPUT [{}]".format(', '.join([str(round(side, 4)) for side in sides])))
            print("OUTPUT Acute Scalene Triangle")
