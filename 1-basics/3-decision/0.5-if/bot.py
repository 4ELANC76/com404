#check whether first number is bigger than the second number.
#Assum first_number and second_number are existing variables.

first_number = input("Please enter your first number.")
first_number = int(first_number)
second_number = input("Please insert your second number")
second_number = int(second_number)

if (first_number > second_number):
  print("First is bigger!")
if (first_number < second_number):
  print("Second is bigger!")
if (first_number == second_number):
  print("No number is bigger!")
print("Done!")
