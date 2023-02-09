import random
from gameLogic import *

# continue playing, valid input
continuePlaying = True
isValidInput = False

# CPU role, player role, player score, cpu score
cpuInput =""
playerInput =""
cpuScore =0
playerScore =0
gameResult =0

input("Welcome to Rock Paper Scissors, press enter to play")

while continuePlaying:
    playerInput =""
    cpuInput =""

    playerInput = input("\nChoose: rock, paper, or scissors: ")
    while(not checkValidInput(playerInput)):
        print("Invalid Input, try again")
        playerInput = input("\nChoose: rock, paper, or scissors: ")

    randomNumber = random.random() * 3

    if randomNumber == 0:
        cpuInput = "rock"
    elif randomNumber == 1:
        cpuInput = "paper"
    else:
        cpuInput = "scissors"

    gameResult = isWinner(playerInput, cpuInput)

    if gameResult == 1:
        playerScore+=1
        print(f"Cpu chose {cpuInput}. You win\nYou gain one point")
    elif gameResult == -1:
        cpuScore+=1
        print(f"Cpu chose {cpuInput}. You lose\nCpu gain one point")
    elif gameResult == 0:
        print("Draw, no winner")

    continuePlaying = playAgain()

print(f"Thank you for playing RPC\nPlayer Score: {playerScore}\nCPU Score: {cpuScore}")