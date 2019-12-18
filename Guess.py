# mini projet sur le jeu "guess the number"
import random


def replay():
    redo = input("another run ? enter yes or no")
    if redo == 'yes':
        numberguess()
    else:
        exit()


def numberguess():
    print("Guess the number between 0 and 20\n")
    print("You got 5 try\n")
    guess = random.randint(0, 20)
    vie = 5
    a = int(input("Give your guess: \n"))
    while a != guess:
        if a not in range(0, 21):  # j'ai pas de signe supérieur sur mon clavier donc j'ai improvisé
            print("Between 0 and 20 only ;p\n")
            a = int(input("Give your guess \n"))
        elif vie != 0:
            if a > guess:
                print("Wrong guess :p\n")
                print("Your guess is too high\n")
            else:
                print("Wrong guess :p \n")
                print("your guess is too low\n")
            a = int(input("try again"))
            vie = vie - 1
            print('You got ', vie, ' live left\n')
        else:
            print("Too bad you lost\n")
            print("The correct guess was\n", guess)
            replay()
    print('Congratulation, you win with', vie, 'live left')
    replay()


numberguess()
