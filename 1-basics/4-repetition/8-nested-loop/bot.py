#The program should start by asking the user how many rows and columns they would like.
#The program should then display a grid of ascii faces where the size of grid matches the number of rows and columns specified by the user.



print("How many rows should I have?")
rows = int(input())

print("How many columns should I have?")
columns = int(input())

print ("Here I go:")

for count in range(0, rows, 1):
    for number in range(0, columns, 1):
        print(":-)", end="")
    print()
