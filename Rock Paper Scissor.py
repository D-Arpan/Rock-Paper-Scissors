'''

WORKFLOW OF THE PROJECT :
    1. Input from the user (Rock, Paper, Scissor)
    2. Computer choice (Random)
    3. Result print


CASES:
    A. Rock
    
    Rock - Rock = Tie
    Rock - Paper = Paper Win
    Rock - Scissors = Rock Win

    B. Paper

    Paper - Paper = Tie
    Paper - Rock = Paper Win
    Paper - Scissors = Scissors Win

    C. Scissors

    Scissors - Scissors = Tie
    Scissors - Paper = Scissors Win
    Scissors - Rock = Rock Win

'''

import random
rock_paper_scissor = ['Rock', 'Paper', 'Scissors']

while True :
    user_choice = input(f"""\nALLOWED MOVES ARE :   
ROCK
PAPER
SCISSORS
    
EXIT - To leave the game
    
YOUR MOVE : """)
    print("")
    comp_choice = random.choice(rock_paper_scissor)

    if user_choice == 'Rock' or user_choice == 'rock' or user_choice =='ROCK':
        print(f"You chose {user_choice.upper()}")
        if comp_choice == 'Rock':
            print (f"Computer chose {comp_choice.upper()}")
            print (f"It is a tie.".upper())
        elif comp_choice == 'Paper':
            print (f"Computer chose {comp_choice.upper()}")
            print (f"Computer Won. Better Luck next time.".upper())
        elif comp_choice == 'Scissors':
            print (f"Computer chose {comp_choice.upper()}")
            print (f"Congrats. You won.".upper())
        else:
            print('Wrong Input')

    elif user_choice == 'Paper' or user_choice == 'paper' or user_choice =='PAPER':
        print(f"You chose {user_choice.upper()}")
        if comp_choice == 'Paper':
            print (f"Computer chose {comp_choice.upper()}")
            print (f"It is a tie.".upper())
        elif comp_choice == 'Scissors':
            print (f"Computer chose {comp_choice.upper()}")
            print (f"Computer Won. Better Luck next time.".upper())
        elif comp_choice == 'Rock':
            print (f"Computer chose {comp_choice.upper()}")
            print (f"Congrats. You won.".upper())
        else:
            print('Wrong Input')

    elif user_choice == 'Scissors' or user_choice == 'scissors' or user_choice =='SCISSORS':
        print(f"You chose {user_choice.upper()}")
        if comp_choice == 'Scissors':
            print (f"Computer chose {comp_choice.upper()}")
            print (f"It is a tie.".upper())
        elif comp_choice == 'Rock':
            print (f"Computer chose {comp_choice.upper()}")
            print (f"Computer Won. Better Luck next time.".upper())
        elif comp_choice == 'Paper':
            print (f"Computer chose {comp_choice.upper()}")
            print (f"Congrats. You won.".upper())
        else:
            print('Wrong Input')

    elif user_choice == 'Exit' or user_choice == 'exit' or user_choice == 'EXIT':
        print(f"The game is closing...\n")

        break

    else:
        print('Wrong input by the user.')
