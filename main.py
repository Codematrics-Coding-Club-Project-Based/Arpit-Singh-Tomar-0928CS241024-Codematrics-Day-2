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



# Feature 2: Factorial Calculator
def calculate_factorial():
    print("Factorial Calculator (n!)")

    try:
        n = int(input("Enter a positive integer: "))
        if n < 0:
            print("Please enter a positive integer.")
            return
        result = math.factorial(n)
        print(f"The factorial of {n} is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")





# Define Main Function for the program
def main():
    print("Welcome to the Python calculator!")

    while True:

        print("\n Please select a Feature to use: ")
        print("1. Quadratic Equation Calculator")
        print("2. Factorial Calculator")
        print("3. Exit")

        choice = input("Enter a choice (1-3): ")

        if choice == "1":
            solve_quadratic()

        elif choice == "2":
            calculate_factorial()

        elif choice == "3":

            print("Exiting the calculator program. Goodbye!")
            sys.exit()
            
        else :
            print("Invalid choice. Please select a valid option (1-3). ")

main()
