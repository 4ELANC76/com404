#create the display box
def display_box(name):
  print("*" * (len(name) + 10))
  print("* Hello", name, "*")
  print("*" * (len(name) + 10))
 
#create the user defined function
def greet_user():
  print("Please enter your name")
  name = str(input())
  display_box(name)
  
greet_user()

#call the function 3 times - the whole thing 3 times
greet_user()
greet_user()
greet_user()
