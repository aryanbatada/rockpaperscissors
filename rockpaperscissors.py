import random


def play_again():
    playornot = input("Would you like to play again?(Y/N)").lower().replace(" ", "")
    while playornot not in ("y","n"):
        print("Seems like you made a typo, try again!")
        playornot = input("Would you like to play again?(Y/N)").lower().replace(" ", "")
    if playornot == "y":
        user_roll()


def user_roll():
    wins = 0
    rounds = []
    draws = 0
    while len(rounds) < 3:
        AI_roll = random.choice(["rock","paper","scissors"])        
        user_pick = input("Do you choose rock, paper, or scissors?").lower().replace(" ", "")
        while user_pick not in ("rock","paper","scissors"):
            print("Seems like you made a typo, try again!")
            user_pick = input("Do you choose rock, paper, or scissors?").lower().replace(" ", "")
        if (user_pick,AI_roll) in (("rock","scissors"),("paper","rock"),("scissors","paper")):
            wins += 1
            rounds.append(1)
            print(f"You won Round {len(rounds)}!")
        elif user_pick == AI_roll:
            draws += 1
            print("It's a draw! Rematch!")
        else:
            rounds.append(1)
            print(f"You lost Round {len(rounds)}!")
    draws += 3
    if wins >= 2:
        print(f"You've won the game! You won {wins} times out of {3+draws}!")
        play_again()
    if wins < 2:
        print(f"You've lost the game! You won {wins} time out of {3+draws}!")
        play_again()

user_roll()