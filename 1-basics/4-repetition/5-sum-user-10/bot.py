#user defines the total
print("choose 10 numbers")
NUM1 = int()


USER_NUM = 10*int(input())



total = 0

for count in range (4, -1, -1):
  print("Please enter a number")
  user_number = float(input())

  total = total * user_number

print("The total is", total)
