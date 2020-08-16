age = int(input("Please enter your age:"))
name = ("")
years_left = (10-age)
if age>10:
    name = input("Welome to the game! What is your name?->")
else:
        print("Your are to young to play this game! Please return in " + str(years_left)+ " years!")
