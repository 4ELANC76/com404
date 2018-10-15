print("Where should I look?")
place = input()

if (place == "in the bedroom"):
  print("Where in the bedroom should I look?")
  bedroom_place = input()
  if (bedroom_place == "under the bed"):
    print("Found some shoes but no battery.")
  elif(bedroom_place != "under the bed"):
    print("Found some mess but no battery.")

  
if (place == "in the bathroom"):
  print("Where in the bathroom should I look?")
  bathroom_place = input()
  if (bathroom_place == "in the bathtub"):
    print("Found a rubber duck but no battery.")
  elif(bathroom_place != "in the bathtub"):
    print("It is wet but I found no battery.")


if (place == "in the lab"):
  print("Where in the lab should I look?")
  lab_place = input()
  if (lab_place == "on the table"):
    print("Yes! I found my battery!")
  elif(lab_place != "on the table"):
    print("Found some tools but no battery.")
  
else:
    print("I do not know where that is but I will keep looking.")
