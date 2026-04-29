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


# Feature 3: Matrix Utilities (Pure Python Implementation)

def create_matrix(rows, cols, name):
    print(f"Creating {name} Matrix ({rows}x{cols})")
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            while True:
                try:
                    value = float(input(f"Enter value for {name}[{i+1}][{j+1}]: "))
                    row.append(value)
                    break
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
        matrix.append(row)
    return matrix

def add_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        print("Error: Matrices must have the same dimensions for addition.")
        return None
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result

def subtract_matrices(matrix_a, matrix_b):
    if len(matrix_a) != len(matrix_b) or len(matrix_a[0]) != len(matrix_b[0]):
        print("Error: Matrices must have the same dimensions for subtraction.")
        return None
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[0])):
            row.append(matrix_a[i][j] - matrix_b[i][j])
        result.append(row)
    return result

def multiply_matrices(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        print("Error: Number of columns in the first matrix must equal the number of rows in the second matrix for multiplication.")
        return None
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            sum_product = 0
            for k in range(len(matrix_a[0])):
                sum_product += matrix_a[i][k] * matrix_b[k][j]
            row.append(sum_product)
        result.append(row)
    return result

def transpose_matrix(matrix):
    result = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix)):
            row.append(matrix[i][j])
        result.append(row)
    return result

def determinant(matrix):
    if len(matrix) != len(matrix[0]):
        print("Error: Determinant can only be calculated for square matrices.")
        return None
    if len(matrix) == 1:
        return matrix[0][0]
    if len(matrix) == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for c in range(len(matrix)):
        sub_matrix = [row[:c] + row[c+1:] for row in matrix[1:]]
        det += ((-1)**c) * matrix[0][c] * determinant(sub_matrix)
    return det

def inverse_matrix(matrix):
    det = determinant(matrix)
    if det == 0:
        print("Error: Matrix is singular and cannot be inverted.")
        return None
    if len(matrix) == 1:
        return [[1 / matrix[0][0]]]
    
    # Calculate the cofactor matrix
    cofactor_matrix = []
    for i in range(len(matrix)):
        cofactor_row = []
        for j in range(len(matrix)):
            sub_matrix = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            cofactor_row.append(((-1)**(i+j)) * determinant(sub_matrix))
        cofactor_matrix.append(cofactor_row)
    
    # Transpose the cofactor matrix to get the adjugate
    adjugate = transpose_matrix(cofactor_matrix)
    
    # Divide the adjugate by the determinant to get the inverse
    inverse = []
    for i in range(len(adjugate)):
        row = []
        for j in range(len(adjugate[0])):
            row.append(adjugate[i][j] / det)
        inverse.append(row)
    
    return inverse

def display_matrix(matrix):
    for row in matrix:
        print(" ".join(f"{value:.2f}" for value in row))    

def matrix_operations():
    while True:
        print("\nMatrix Operations")
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        print("4. Transpose Matrix")
        print("5. Determinant of Matrix")
        print("6. Inverse of Matrix")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice in ["1", "2", "3"]:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))

            A = create_matrix(rows, cols, "A")
            B = create_matrix(rows, cols, "B")

            if choice == "1":
                result = add_matrices(A, B)
            elif choice == "2":
                result = subtract_matrices(A, B)
            elif choice == "3":
                result = multiply_matrices(A, B)

            if result:
                print("Result:")
                display_matrix(result)

        elif choice == "4":
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))
            A = create_matrix(rows, cols, "A")

            result = transpose_matrix(A)
            print("Transpose:")
            display_matrix(result)

        elif choice == "5":
            n = int(input("Enter size of square matrix (n x n): "))
            A = create_matrix(n, n, "A")

            det = determinant(A)
            print(f"Determinant: {det}")

        elif choice == "6":
            n = int(input("Enter size of square matrix (n x n): "))
            A = create_matrix(n, n, "A")

            inv = inverse_matrix(A)
            if inv:
                print("Inverse:")
                display_matrix(inv)

        elif choice == "7":
            break

        else:
            print("Invalid choice. Try again.")


# Feature 4: Square root calculator feature

def calculate_square_root():
    print("Square Root Calculator")

    try:
        number = float(input("Enter a non-negative number: "))
        if number < 0:
            print("Please enter a non-negative number.")
            return
        result = math.sqrt(number)
        print(f"The square root of {number} is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


# Feature 5: Power Calculator (x^y)

def calculate_power():
    print("Power Calculator (x^y)")

    try:
        base = float(input("Enter the base (x): "))
        exponent = float(input("Enter the exponent (y): "))
        result = math.pow(base, exponent)
        print(f"{base} raised to the power of {exponent} is {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers for base and exponent.")


# Feature 6: Linear Equation Solver (Gaussian Elimination Method)

def solve_linear_equations():
    print("Linear Equation Solver (Gaussian Elimination)")

    try:
        n = int(input("Enter the number of variables: "))
        A = []
        b = []

        print("Enter the coefficients of the equations:")
        for i in range(n):
            row = []
            for j in range(n):
                value = float(input(f"Coefficient of variable {j+1} in equation {i+1}: "))
                row.append(value)
            A.append(row)
            constant = float(input(f"Constant term for equation {i+1}: "))
            b.append(constant)

        # Forward elimination
        for i in range(n):
            for j in range(i+1, n):
                factor = A[j][i] / A[i][i]
                for k in range(i, n):
                    A[j][k] -= factor * A[i][k]
                b[j] -= factor * b[i]

        # Back substitution
        x = [0] * n
        for i in range(n-1, -1, -1):
            x[i] = (b[i] - sum(A[i][j] * x[j] for j in range(i+1, n))) / A[i][i]

        print("Solution:")
        for i in range(n):
            print(f"x{i+1} = {x[i]}")

    except ValueError:
        print("Invalid input. Please enter valid numbers and integers where required.")


# Feature 7: Temperature Converter(Celcius to Fahrenheit and vice versa)

def temperature_converter():
    print("Temperature Converter")

    try:
        choice = input("Convert from (1) Celsius to Fahrenheit or (2) Fahrenheit to Celsius? Enter 1 or 2: ")

        if choice == "1":
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C is equal to {fahrenheit}°F")

        elif choice == "2":
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is equal to {celsius}°C")

        else:
            print("Invalid choice. Please enter 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter a valid number for temperature.")


# Feature 8: Length Converter (Meters to Feet,kilometers , centimeters , etc and vice versa)

def length_converter():
    print("Length Converter")

    try:
        choice = input("Convert from (1) Meters to Feet or (2) Feet to Meters? Enter 1 or 2: ")

        if choice == "1":
            meters = float(input("Enter length in meters: "))
            feet = meters * 3.28084
            print(f"{meters} meters is equal to {feet} feet")

        elif choice == "2":
            feet = float(input("Enter length in feet: "))
            meters = feet / 3.28084
            print(f"{feet} feet is equal to {meters} meters")

        else:
            print("Invalid choice. Please enter 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter a valid number for length.")



# Feature 9: Area and Perimeter calculator for different shapes(circle, rectangle, triangle, etc)


def area_perimeter_calculator():
    print("Area and Perimeter Calculator")

    try:
        shape = input("Select a shape (circle, rectangle, triangle): ").lower()

        if shape == "circle":
            radius = float(input("Enter the radius of the circle: "))
            area = math.pi * radius**2
            perimeter = 2 * math.pi * radius
            print(f"Area of the circle: {area}")
            print(f"Perimeter of the circle: {perimeter}")

        elif shape == "rectangle":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            area = length * width
            perimeter = 2 * (length + width)
            print(f"Area of the rectangle: {area}")
            print(f"Perimeter of the rectangle: {perimeter}")

        elif shape == "triangle":
            base = float(input("Enter the base of the triangle: "))
            height = float(input("Enter the height of the triangle: "))
            area = 0.5 * base * height
            side1 = float(input("Enter length of side 1: "))
            side2 = float(input("Enter length of side 2: "))
            side3 = float(input("Enter length of side 3: "))
            perimeter = side1 + side2 + side3
            print(f"Area of the triangle: {area}")
            print(f"Perimeter of the triangle: {perimeter}")

        else:
            print("Invalid shape. Please select from circle, rectangle, or triangle.")

    except ValueError:
        print("Invalid input. Please enter valid numbers for dimensions.")


# Feature 9: Volume Calculator for different shapes (circle , rectangle, triangle, etc)

def volume_calculator():
    print("Volume Calculator")

    try:
        shape = input("Select a shape (sphere, cube, cylinder): ").lower()

        if shape == "sphere":
            radius = float(input("Enter the radius of the sphere: "))
            volume = (4/3) * math.pi * radius**3
            print(f"Volume of the sphere: {volume}")

        elif shape == "cube":
            side = float(input("Enter the side length of the cube: "))
            volume = side**3
            print(f"Volume of the cube: {volume}")

        elif shape == "cylinder":
            radius = float(input("Enter the radius of the cylinder: "))
            height = float(input("Enter the height of the cylinder: "))
            volume = math.pi * radius**2 * height
            print(f"Volume of the cylinder: {volume}")

        else:
            print("Invalid shape. Please select from sphere, cube, or cylinder.")

    except ValueError:
        print("Invalid input. Please enter valid numbers for dimensions.")



# Feature 10: Volume converter (cubic meters to liters, cubic feet to gallons, etc and vice versa)

def volume_converter():
    print("Volume Converter")

    try:
        choice = input("Convert from (1) Cubic Meters to Liters or (2) Liters to Cubic Meters? Enter 1 or 2: ")

        if choice == "1":
            cubic_meters = float(input("Enter volume in cubic meters: "))
            liters = cubic_meters * 1000
            print(f"{cubic_meters} cubic meters is equal to {liters} liters")

        elif choice == "2":
            liters = float(input("Enter volume in liters: "))
            cubic_meters = liters / 1000
            print(f"{liters} liters is equal to {cubic_meters} cubic meters")

        else:
            print("Invalid choice. Please enter 1 or 2.")

    except ValueError:
        print("Invalid input. Please enter a valid number for volume.")
        


# Define Main Function for the program
def main():
    print("Welcome to the Python calculator!")

    while True:

        print("\n Please select a Feature to use: ")
        print("1. Quadratic Equation Calculator")
        print("2. Factorial Calculator")
        print("3. Matrix Utilities")
        print("4. Square Root Calculator")
        print("5. Power Calculator")
        print("6. Temperature Converter")
        print("7. Length Converter")
        print("8. Area and Perimeter Calculator")
        print("9. Volume Calculator")
        print("10. Volume Converter")
        print("11. Exit")

        choice = input("Enter a choice (1-11): ")

        if choice == "1":
            solve_quadratic()

        elif choice == "2":
            calculate_factorial()

        elif choice == "3":
            matrix_operations()

        elif choice == "4":
            calculate_square_root()


        elif choice == "5":
            calculate_power()

        elif choice == "6":
            temperature_converter()

        elif choice == "7":
            length_converter()

        elif choice == "8":
            area_perimeter_calculator()

        elif choice == "9":
            volume_calculator()

        elif choice == "10":
            volume_converter()

        elif choice == "11":
            print("Exiting the calculator program. Goodbye!")
            sys.exit()

        else:
            print("Invalid choice. Please select a valid option (1-11). ")


main()
