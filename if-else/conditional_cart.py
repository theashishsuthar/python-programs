
sam_age = 10

if sam_age < 9:
    breakfast = "milk porridge"
elif 10 <= sam_age <= 14:
    breakfast = "sandwich"
elif 15 <= sam_age <= 17:
    breakfast = "burger"
else:
    breakfast = "unknown"

print(f"The canteen master will offer Sam a {breakfast} for breakfast.")
