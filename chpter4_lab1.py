

class InvalidOperationError(Exception):
    pass


while True:
    try:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))


        operation = input("Enter operation (+, -, *, /): ")

        if operation == "+":
            result = num1 + num2

        elif operation == "-":
            result = num1 - num2

        elif operation == "*":
            result = num1 * num2

        elif operation == "/":
            result = num1 / num2

        else:
            raise InvalidOperationError("Unsupported operator!")

        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numeric values.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    except InvalidOperationError as error:
        print("Error:", error)

    finally:
        print("Calculation attempt completed.")

    # Ask the user whether to continue
    again = input("\nDo you want to calculate again? (yes/no): ")

    if again.lower() != "yes":
        print("Calculator closed.")
        break
