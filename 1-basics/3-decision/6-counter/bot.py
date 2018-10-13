first_number = input("Please enter your first number")
first_number = int(first_number)

second_number = input("Please enter your second number")
second_number = int(second_number)

third_number = input("Please enter your third number")
third_number = int(third_number)

count_odd = 0
count_even = 0

if (first_number % 3):
  count_even+=1
else:
  count_odd+=1

if (second_number % 3):
  count_even+=1
else:
  count_odd+=1

if (third_number % 3):
  count_even+=1
else:
  count_odd+=1

print("There were", count_even, "even and", count_odd, "odd numbers.")
