#add up the ages of the ponies and return it
def sum_ages_of_friends(applejack_age, rainbowdash_age, buttershine_age):
  total = (applejack_age + rainbowdash_age + buttershine_age)
  return total


#add up the ages of the ponies and divide it by the number of ponies to work out the average. It will then return it
def calc_avg_age_of_friends(applejack_age, rainbowdash_age, buttershine_age):
  total = sum_ages_of_friends(applejack_age, rainbowdash_age, buttershine_age)/ 3
  return total

def run():
  print("What is the age of Applejack? ")
  a_age = int(input())

  print("What is the age of Rainbowdash? ")
  r_age = int(input())

  print("What is the age of Buttershine? ")
  b_age = int(input())

  print("Would you like the sum or average?")
  n = str(input())

  if (n == "sum"):
    print( sum_ages_of_friends(a_age, r_age, b_age) )
  elif(n == "average"):
    print(calc_avg_age_of_friends(a_age, r_age, b_age))

run()
