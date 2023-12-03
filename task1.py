def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot perform division by zero."


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("Choose the operation you want to perform on the numbers:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter choice: ")

if choice == '1':
    result = addition(num1, num2)
    op = "+"
elif choice == '2':
    result = subtraction(num1, num2)
    op = "-"
elif choice == '3':
    result = multiplication(num1, num2)
    op = "*"
elif choice == '4':
    result = division(num1, num2)
    op = "/"
else:
    print("Invalid Input")
    exit()

print(f"{num1} {op} {num2} = {result}")
