def robot_activity():
  print("What activity should I do?")
  activity = str(input())

  if(activity == "watch movie"):
    print("watching a movie sounds like fun.")
  elif(activity == "play"):
    print("I have lots of toys to play with.")
  else:
    print("I am not sure if I will like it but I will give it a try.")

robot_activity()
