from random import randint
from gameComponents import winLose, gameVars, playingGame

# set up pur game loop so that we can keep playing and not exit

print("==============================")
print("Welcome to Rock Paper Scissors OF DEATH!!! (Not Really)")

while gameVars.player is False: 
    print("==============================")
    gameVars.player = input("Choose your weapon: rock, paper or scissors: ")
    print("==============================")
    gameVars.computer = gameVars.choices[randint(0, 2)]

    print("player chose: " + gameVars.player)
    print("computer chose: " + gameVars.computer)

    playingGame.game()
    print("player life count: " + str(gameVars.playerLives))
    print("computer life count: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        print("==============================")
        winLose.winorlose("Lost")
        
    elif gameVars.computerLives == 0:
        print("==============================")
        winLose.winorlose("Won")
        
    gameVars.player = False
