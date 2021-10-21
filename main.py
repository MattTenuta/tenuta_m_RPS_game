from random import randint

# player will be the weapon the player chooses via input
player = input("Choose your weapon: Rock, Paper or Scissors: ")

choices = ["rock", "paper", "scissors"]

computer = choices[randint(0, 2)]

#these lives need to decrement when a player loses a round
playerLives = 5
computerLives = 5

print("player chose: " + player)
print("computer chose: " + computer)