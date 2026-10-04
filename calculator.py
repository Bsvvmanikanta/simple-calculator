# Simple Calculator
# This program performs basic arithmetic operations.

# Taking input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("\nChoose an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

choice = input("Enter your choice (1/2/3/4): ")

# Performing the selected operation
if choice == "1":
    result = num1 + num2
    print("Result:", result)

elif choice == "2":
    result = num1 - num2
    print("Result:", result)

elif choice == "3":
    result = num1 * num2
    print("Result:", result)

elif choice == "4":
    try:
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

else:
    print("Invalid choice. Please select 1, 2, 3, or 4.")
