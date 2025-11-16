#Function that returns the quadratic formula output

import math

def quad_form():
    
    a = float(input("Enter 'a' : "))
    b = float(input("Enter 'b' : "))
    c = float(input("Enter 'c' : "))

    discriminant = b**2 - 4*a*c

    if discriminant<0:
        return "No real","roots"
    else:
        minus = ((-b) - math.sqrt(discriminant))/(2*a)
        plus = ((-b) + math.sqrt(discriminant))/(2*a)

        return minus,plus

lambda1, lambda2 = quad_form()

print(lambda1, lambda2)
