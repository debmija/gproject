print("Welcome to the Simple Calculator")

def addition(num1, num2):
    print(f"{num1} + {num2} = {num1 + num2}")

def subtraction(num1, num2):
    print(f"{num1} - {num2} = {num1 - num2}")

def multiplication(num1, num2):
    print(f"{num1} X {num2} = {num1 * num2}")

def division(num1, num2):
    if num2 == 0:
        print("Undefined")
        return
    print(f"{num1} / {num2} = {num1 / num2}")




menu = """
Select operation:
ADD. Addition
SUB. Subtraction
MUL. Multiplication
DIV. Division
Q. Exit
"""

while True:
    print(menu)
    choice = input("Enter your choice from 1 to 5: ").strip().upper()

    if choice == "Q":
        print("Quitting...")
        break

    if choice not in ["ADD", "MUL", "DIV", "SUB"]:
        print("Invalid choice.")
        continue

    first_num = float(input("Enter first number: "))
    second_num = float(input("Enter second number: "))

    if choice == "ADD":
        addition(first_num, second_num)
    elif choice == "SUB":
        subtraction(first_num, second_num)
    elif choice == "MUL":
        multiplication(first_num, second_num)
    elif choice == "DIV":
        division(first_num, second_num)
