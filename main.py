import math
import statistics
import sys

# Feature 1: Calculator solve Quadratic Equations Solver

def solve_quadratic():
    print ("Quadratic Equation Solver (ax^2 + bx + c = 0)")

    try:
        a = float(input("Enter The Coefficient a: "))
        b = float(input("Enter The Coefficient b: "))
        c = float(input("Enter The Coefficient c: "))

        if a == 0:
            print("Coefficient a cannot be zero for a quadratic equation.")
            return
        d = b**2 - 4*a*c
        if d > 0:
            root1 = (-b + math.sqrt(d)) / (2*a)
            root2 = (-b - math.sqrt(d)) / (2*a)
            print(f"The roots are real and different: {root1} and {root2}")
        elif d == 0:
            root = -b / (2*a)
            print(f"The roots are real and the same: {root}")
        else:
            real_part = -b / (2*a)
            imaginary_part = math.sqrt(-d) / (2*a)
            print(f"The roots are complex: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")    

    except ValueError:
        print("Invalid input. Please enter numeric values for a, b, and c.")    

solve_quadratic()