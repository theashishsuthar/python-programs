# Problem 5: Ticket Price Calculator
# Write a program that calculates the ticket price for a movie theater based on the age of the customer. The program should ask the user for their age and then calculate the ticket price as follows:

# Children under 5: Free
# Children aged 5-12: $10
# Adults aged 13-64: $15
# Seniors 65 and above: $12


age = int(input("Enter your age: "))

if age < 5:
    ticket_price = 0
elif age <= 12:
    ticket_price = 10
elif age <= 64:
    ticket_price = 15
else:
    ticket_price = 12

print(f"The ticket price is ${ticket_price}.")
