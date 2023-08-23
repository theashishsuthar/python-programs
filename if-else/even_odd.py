# Problem 6: Even or Odd Checker
# Write a program that takes an integer as input and determines whether it's even or odd.

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
