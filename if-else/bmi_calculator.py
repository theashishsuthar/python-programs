# Write a program that calculates the Body Mass Index (BMI) of a person. The program should take the person's weight in kilograms and height in meters as inputs, and then print out their BMI along with an appropriate message indicating whether they are underweight, normal weight, overweight, or obese.

weight = float(input("Enter your weight in kilograms: "))
height = float(input("Enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    category = "underweight"
elif bmi < 24.9:
    category = "normal weight"
elif bmi < 29.9:
    category = "overweight"
else:
    category = "obese"

print(f"Your BMI is {bmi:.2f}, which is considered {category}.")
