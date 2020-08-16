# Welcome to my Dice Game
import random
import datetime
# Create an Object for the Players with the parameters name and score
class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def getName(self):
        return self.name

    def getScore(self):
        return self.score

    def setName(self, new_name):
        self.name = new_name

    def updateScore(self, newpoints):
        self.score = self.score + newpoints
        if self.score < 0:
            self.score = 0


class Scores:
    def __init__(self, username, score, date):
        self.username = username
        self.score = score
        self.date = date

    def getUsername(self):
        return self.username

    def getScore(self):
        return self.score

    def setUsername(self, newUsername):
        self.username = newUsername

    def setScore(self, newScore):
        self.score = newScore

    def setDate(self, newDate):
        self.date = newDate




# *************Global Variables*************
player1 = Player("", 0)  # initialise a new player object for player1
player2 = Player("", 0)  # initialise a new player object for player2
menuOption = ""
buttonPressed = ""

# ======================================MENU OPTIONS======================================
def Menu():
    global menuOption
    while menuOption != "Q":
        printMenu()
        if menuOption == "P1":
            Login("1")

        if menuOption == "P2":
            Login("2")

        if menuOption == "S":
            # Checks to see that all players have logged in before starting the game
            if player1.name == "" and player2.name == "":
                print("\nPlayer 1 and 2 have not logged in")
            elif player1.name == "":
                print("\nPlayer 1 has not logged in")
            elif player2.name == "":
                print("\nPlayer 2 has not logged in")
            else:
                startGame()

        if menuOption == "L":
            displayLeaderBoard()

    print("\n\nThank you for Playing!")


def printMenu():
    global menuOption

    print("\n------------Menu------------\n"
          "Player 1: " + playersLoggedIn(player1) + "\n"
                                                    "Player 2: " + playersLoggedIn(player2) + "\n\n"
                                                                                              "'P1' - Login as Player 1\n"
                                                                                              "'P2' - Login as Player 2\n"
                                                                                              "'S' - Start Game\n"
                                                                                              "'L' - Top 5 Scores\n"
                                                                                              "'Q' - Quit Game"
          )
    menuOption = input("Choose one of the options above: ").upper()


def playersLoggedIn(Player):
    if Player.name == "":
        return "Not Signed in"
    else:
        return Player.name


# -----------------------------------------LOGIN----------------------------------------
# Allows player to login by authenticating their username and password
def Login(playerNum):
    global player1
    global player2
    print("\nPlayer " + playerNum + " Login")
    playerEuthenticated = False
    global buttonPressed
    buttonPressed = ""

    while not playerEuthenticated and buttonPressed != "B":
        playerUsername = input("Enter your username: ")
        playerPassword = input("Enter your password: ")

        loginFile = open("UserLogins.txt", "a")  # "a" will open the file or create a new one if the file does not exist
        loginFile = open("UserLogins.txt", "r")  # "r" makes the file readable

        # Loop through each line of the file. When reading a line, split the line up using commas.
        # Once the line has been split up, we can assume that the first item in the list is the username
        # and the second item is the password. These are compared with the username and password entered
        # by the user to authenticate the login.
        for line in loginFile.read().splitlines():
            login = line.split(",")
            if login[0] == playerUsername and login[1] == playerPassword:
                playerEuthenticated = True
                break

        if playerEuthenticated:
            if playerNum == "1":
                player1.setName(playerUsername)
            elif playerNum == "2":
                player2.setName(playerUsername)
            print(playerUsername + " signed in as player " + playerNum + "!")

        else:
            print("Login incorrect!")
            while True:
                buttonPressed = input("Enter 'R' to try again or 'B' to go back to the Menu: ").upper()
                if buttonPressed == "R":
                    break
                elif buttonPressed == "B":
                    break
                else:
                    print("Invalid Selection!! Try Again!")


# -----------------------------------------START GAME--------------------------------------
def startGame():
    global player1
    global player2
    dice1 = 0
    dice2 = 0
    diceTotal = 0
    totalRounds = 5
    gameActive = True
    buttonPressed = ""

    while gameActive and buttonPressed != "Q":

        # Start 5 rounds
        for roundNum in range(totalRounds): #loops from 0 to 4 when totalRounds is 5
            print("\n\n------------------------ROUND " + str(roundNum + 1) + "/" + str(
                totalRounds) + "------------------------\n")

            # player1's turn
            takeTurn(player1, dice1, dice2, diceTotal)
            if player1.score < 0:
                print(player1.name + " has Lost! Your score went below 0!")
                playerWon()
                break

            # player2's turn
            takeTurn(player2, dice1, dice2, diceTotal)
            if player2.score < 0:
                print(player2.name + " has Lost! Your score went below 0!")
                playerWon()
                break

            endOfRoundStats(roundNum + 1, player1, player2)

        if player1.score == player2.score:
            suddenDeath(dice1, dice2)
        else:
            playerWon()
            updateLeaderboard(player1)
            updateLeaderboard(player2)
            player1.score = 0
            player2.score = 0


        gameActive = False

        if buttonPressed == "E":
            print("Game Ended")
        else:
            print("Finished")


# -----------------------------------------LEADERBOARD--------------------------------------
def displayLeaderBoard():
    orderedScores = [] #Initialised new list (list of objects)


    scoresFile = open("Scores.txt", "r")  # "r" makes the file readable

    for line in scoresFile.read().splitlines(): # Loop through each line
        scoreData = line.split(",")  # Split the line using commas
        scoreObj = Scores(scoreData[0], int(scoreData[1]), scoreData[2]) # Storing each line as an object using parameters
        orderedScores.append(scoreObj) # add the score object into the list

    orderedScores.sort(key=lambda x: x.score, reverse=True) # sorts it from low to high so we reverse the order

    print("\n\n----------------------LEADERBOARD----------------------\n")
    for i in range(5):
        num = i+1
        print(str(num) + "." +
              "  User - " + str(orderedScores[i].username) +
              "  Score - " + str(orderedScores[i].score) +
              "  Date - " + str(orderedScores[i].date) + "\n")

        if len(orderedScores)-1 == i:
            break



def updateLeaderboard(player):
    username = player.name
    score = player.score
    date = datetime.date.today()

    with open("Scores.txt", "a") as loginFile: # "a" will open the file or create a new one if the file does not exist
        loginFile.write(str(username) + "," + str(score) + "," + str(date) + "\n")

# -----------------------------------------END GAME--------------------------------------
def endGame():
    None


# =================================GAME LOGIC=================================
def takeTurn(p, d1, d2, dt):
    print("\n\n************* " + p.name + "'s turn *************")
    d1 = rollDice()
    d2 = rollDice()

    dt = d1 + d2

    p.updateScore(dt)  # add dice total to the players score

    checkDiceOddEven(p, dt)  # add or subtracts points depending on odd or even score

    checkDouble(p, d1, d2)  # extra go if you roll a double


def rollDice():
    while True:
        buttonPressed = input("Press R to roll dice...").upper()
        if buttonPressed == "R":
            numRolled = random.randint(1, 7) # generate a random number from 1 to 6
            print("You rolled a " + str(numRolled) + "\n")
            return numRolled


def checkDiceOddEven(p, dt):
    if dt % 2 == 0:  # Even
        p.updateScore(10)
        print("Well done, your total was even! Here's an extra 10 points! (+10)")
    else:  # Odd
        p.updateScore(-5)
        print("Oh no, you have an odd total! That's minus 5 points (-5)")


def checkDouble(player, d1, d2):
    if d1 == d2:
        print("You rolled a Double! You get to roll 1 dice again!")
        d1 = rollDice()
        player.updateScore(d1)
        print("This will be added to your total! (+" + str(d1) + ")")


def endOfRoundStats(round, p1, p2):
    print("\n\n////////// At the end of Round " + str(round) + ":\n"
          + p1.getName() + " has " + str(p1.getScore()) + " points\n"
          + p2.getName() + " has " + str(p2.getScore()) + " points")


def playerWon():
    global player1
    global player2

    if player1.score > player2.score:
        winningMessage(player1)
    else:
        winningMessage(player2)


def winningMessage(player):
    print("\n\n\n"
          "//////////////////////////////////////////////////"
          "Congratulations " + player.name + "! You Win!!!\n")


def suddenDeath(d1, d2):
    global player1
    global player2

    won = False

    print("You have entered SUDDEN DEATH! Heighest score Wins")

    while not won:
        print("\n************* " + player1.name + "'s turn *************")
        d1 = rollDice()

        print("\n************* " + player2.name + "'s turn *************")
        d2 = rollDice()

        if d1 > d2:
            winningMessage(player1)
            won = True
        elif d1 < d2:
            winningMessage(player2)
            won = True
        else:
            print("DRAW! Have another go\n\n")


# //////////////////////////////////////////////////////////////////////////////////////////////////

print("================================Welcome to Dice Roller================================\n\n"
      + "**********************************   TOP 5 SCORES   **********************************")

Menu()

