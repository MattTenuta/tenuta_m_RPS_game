from random import randint
from gameComponents import winLose, gameVars, playingGame

# set up pur game loop so that we can keep playing and not exit
while gameVars.player is False: 
    gameVars.player = input("Choose your weapon: Rock, Paper or Scissors: ")
    gameVars.computer = gameVars.choices[randint(0, 2)]

    print("player chose: " + gameVars.player)
    print("computer chose: " + gameVars.computer)

    playingGame.game()
    print("player life count: " + str(gameVars.playerLives))
    print("computer life count: " + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winLose.winorlose("Lost")
        
    elif gameVars.computerLives == 0:
        winLose.winorlose("Won")
        
    gameVars.player = False
