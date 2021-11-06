from gameComponents import gameVars

def winorlose(status):
    print("You " + status)

    choice = input("Do you want to play again? y/n: ")

    if choice == "n":
        print("========= Rage Quitting Already? You Pathetic Human =========")
        exit()
    elif choice == "y":
            print("==============================")
            print("Let's do this")
            print("Your going down Loser")
            gameVars.playerLives = 2
            gameVars.computerLives = 2
            gameVars.player = False
    
    else:
        print("Good Job, You Broke the Game")
