direction = input("Towards which direction should I paint?")
direction = str(direction)

if (direction == "up"):
  print("I am painting in the upward direction")
elif (direction == "down"):
  print("I am painting in the downward direction")
elif (direction == "left"):
  print("I am painting towards the left")
elif (direction == "right"):
  print("I am painting towards the right")
else:
  print("I am confused which way you want me to paint!")
