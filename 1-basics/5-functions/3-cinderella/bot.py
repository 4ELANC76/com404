#person is a parameter but don't need to define it, it is a value
def try_glass_slipper_on(person):
  if (person == "Cinderella"):
    print("I found my pricess!")
  elif(person == "Eldest step sister"):
    print("You are not my princess. Your feet are too big!")
  else:
    print("You are not my princess. Your feet are too small!")

#The following are calls o the fuction for testing purpose
try_glass_slipper_on("Eldest step sister")
try_glass_slipper_on("Youngest step sister")
try_glass_slipper_on("Cinderella")
