# Problem 1: Grade Calculator
# Write a program that takes a student's score as input and prints out their corresponding letter grade according to the following scale:

# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F

# def grade_calculator(marks):
#     if(marks >=90 and marks <=100):
#         return 'Grade A'
#     elif(marks >=80 and marks <=89):
#         return 'Grade B'
#     elif(marks >=70 and marks <= 79):
#         return 'Grade C'
#     elif(marks >=60 and marks <=69):
#         return 'Grade D'
#     elif(marks <=60):
#         return 'Grade F'
#     else:
#         return 'Wrong input'

# print(grade_calculator(int(input("Enter the student's score: "))))


# Problem 2: Leap Year Checker
# Write a program that takes a year as input and determines whether it's a leap year or not. Leap years are divisible by 4, but not by 100 unless they are also divisible by 400.


year = int(input("Enter a year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
