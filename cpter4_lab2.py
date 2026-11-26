


class InvalidGradeError(Exception):
    pass



def validate_grade(value):


    try:
        grade = float(value)

    except ValueError:
        raise ValueError("Grade must be a numeric value.")


    if grade < 0 or grade > 100:
        raise InvalidGradeError("Grade must be between 0 and 100.")

    return grade



while True:

    value = input("Enter student grade: ")

    try:
        grade = validate_grade(value)

        print("Valid grade:", grade)

    except ValueError as error:
        print("Invalid input:", error)

    except InvalidGradeError as error:
        print("Invalid grade:", error)

   
    again = input("Do you want to test another grade? (yes/no): ")

    if again.lower() != "yes":
        print("Program finished.")
        break
