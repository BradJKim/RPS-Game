def checkValidInput(input):
    validInputs = ("rock", "scissors", "paper")
    for word in validInputs:
            if(input == word):
                return True
    return False

def isWinner(playerInput, cpuInput):
    if playerInput == "rock" and cpuInput == "rock":
        return 0
    if playerInput == "rock" and cpuInput =="paper":
        return -1
    if playerInput == "rock" and cpuInput == "scissors":
        return 1
    if playerInput == "paper" and cpuInput == "rock":
        return 1
    if playerInput == "paper" and cpuInput == "paper":
        return 0
    if playerInput == "paper" and cpuInput == "scissors":
        return -1
    if playerInput == "scissors" and cpuInput == "rock":
        return -1
    if playerInput == "scissors" and cpuInput == "paper":
        return 1
    if playerInput == "scissors" and cpuInput == "scissors":
        return 0    


def playAgain():
    yesNoInput = input("\nWould you like to play again? (y/n)")
    if yesNoInput == "y":
        print("Play Again:")
        return True
    elif yesNoInput == "n": 
        return False
    else:
        print("Invalid Input: Enter y or n:")
        playAgain()
