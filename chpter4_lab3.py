

class DocumentReadError(Exception):
    pass



filename = input("Enter filename: ")

try:

    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()

except FileNotFoundError:
    print("Error: File not found.")

except PermissionError:
    print("Error: Permission denied.")

except UnicodeDecodeError:
    print("Error: File encoding is not UTF-8.")

except OSError as error:
    raise DocumentReadError("Unable to read the document.") from error

else:
    
    print("\nFile content:")
    print(content)

finally:
    print("\nFile reading attempt completed.")
