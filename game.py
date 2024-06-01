
# Game played between player vs computer

# rock_paper_scissor_Game_rule:
#paper beat rock
#rock beat paper
#scissors beat rock 

# logic of the game use of strings, forloops,break statement and conditional statement

# part for player_game:
import random
 # use of for loops
while True:
    print('\n')
    print('1),rock')
    print('2),paper')
    print('3),scissors')
    # selection , need to input choices of the game
    selection = int(input('enter choice: 1 for rock, 2 for scissors, 3 for paper'))

   # conditional statement applies, use: of if ,elif and else for the game logic 
    if(selection == 1):
        player_game = 'rock'
    elif(selection == 2):
        player_game = 'paper'
    else:
        player_game = 'scissors'

        print('\n')
        print('player_choice',player_game)
        # need to print out output:

        # part for Game_choice
#choice of Game_choice u need to pick either rock , paper ,scissors
    Game_choice = ['rock','paper','scissors']

    #Game_choice are picked randomly
    computer_game = random.choice(Game_choice)

    #need to print out the output:
    print('computer_game',computer_game)

# conditinal statement for the logic of the game:
    if(player_game == computer_game):
        print('DRAW!')
    elif (player_game == 'rock'):
        if ( computer_game == 'paper'):
            print('computers Wins!')
    elif(computer_game =='scissors'):
        print('players wins!')
    elif (player_game == 'paper'):
        if (computer_game =='scissors'):
          print('computer wins!')
    elif (computer_game == 'rock'):
        print('players wins!')
    elif (player_game == 'scissors'):
        if(computer_game == 'paper'):
            print('computer wins!')
    elif (computer_game == 'rock'):
        print('players wins!')
    else:
        print('Nobody wins the game!')

        print('\n')

        print('1),start over')
       # output means to start over
        print('2),quit')
        # output means to quit
        if(selection == 2):
             break
            # implies game to start fresh: