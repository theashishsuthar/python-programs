def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

annie_birth_year = 1996
jane_birth_year = 1999

if is_leap_year(annie_birth_year):
    print("Annie was born in a leap year.")
else:
    print("Annie was not born in a leap year.")

if is_leap_year(jane_birth_year):
    print("Jane was born in a leap year.")
else:
    print("Jane was not born in a leap year.")
