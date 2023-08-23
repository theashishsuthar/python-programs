#  Problem 3: Number Comparison
#  Write a program that takes two numbers as input and prints out whether the first number is greater than, equal to, or less than the second number.

first_number = int(input("Enter a first number: "))
second_number = int(input("Enter a second number: "))

if(first_number > second_number):  
    print(f'{first_number} is greater than {second_number}')
elif(first_number == second_number):
    print(f'{first_number} is equal to {second_number}')
elif(first_number < second_number):
    print(f'{first_number} is less than {second_number}')