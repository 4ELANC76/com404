print("what is your name human?")
name = input()

print ("How old are you (in years)?")
years =int(input()) 

print ("How tall are you (in meters)?")
meters = float(input())

print("How much do you weigh (in kilograms)?")
kilograms = int(input())

bmi = kilograms/(meters*meters)
print (name, "you are", years, "years old and your bmi is", bmi,)
