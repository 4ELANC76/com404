#incorrect


def run():
  print("Please enter a character to display")
  character = str(input())

  print("Please enter total number of characters")
  num_character = int(input())

  print("Please enter a whole number")
  num = int(input())

  print("Result is")

  for position in range (0,num_character,1):
    if (position % num == 0):
      print(character, end="") 
    else:
      print("-", end="")

run()
