# A little game of rock paper and scissor

import random


def replay():  # just a replay function
    play = input("Wanna play again yes or no ?\n")
    if play == "yes":
        game()
    else:
        exit()


def game():  # main game code
    win_state = False
    player_win = False
    play = ["paper", "rock", "scissor"]
    play_bot = random.choice(play)
    while not win_state:  # tant qu'il y a pas de vainqueur le jeu continue
        a = input("Play with me ! rock paper or scissor?\n")
        if a == play_bot:
            print("It's a tie !!")
            replay()
        elif play_bot == "paper" and a == "scissor" or play_bot == "rock" and a == "paper" or play_bot == "scissor" and a == "rock":
            player_win = True
            win_state = True
        else:
            win_state = True

    if win_state and player_win is True:
        print("you win, my play was", play_bot)
        replay()
    else:
        print("You lose, my play was", play_bot)
        replay()


game()
