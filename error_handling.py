try:
     number = int(input("Enter a number: "))
     result = 10 / number
     print(result)
except ValueError:
     print("That's not a valid number. Please enter an integer.")

except ZeroDivisionError:
     print("You cannot divide by zero. Please enter a non-zero integer.")