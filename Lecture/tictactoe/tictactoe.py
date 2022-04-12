
#Tic Tac Toe game grid
from idna import check_bidi
from numpy import single


def grid_tic_tac_toe(inputs):
    print("\n")
    print(f"\t [{inputs[0]}] | [{inputs[1]}] | [{inputs[2]}] ")
    print("\n")
    print(f"\t [{inputs[3]}] | [{inputs[4]}] | [{inputs[5]}] ")
    print("\n")
    print(f"\t [{inputs[6]}] | [{inputs[7]}] | [{inputs[8]}] ")
    print("\n")

# print(grid_tic_tac_toe(['X','O','X','X','O','X','X','O','X']))

# Function to check if anyone has won
def check_status(player_pos, cur_player):
    #check Draw
    if len(player_pos['X']) + len(player_pos['O']) == 9:
        return "Draw"

    #check Win
    # 이길 수 있는 모든 경우의 수 -> winning combination
    solution = [[1,2,3], [4,5,6], [7,8,9], 
                [1,5,9], [3,5,7], 
                [1,4,7], [2,5,8], [3,6,9]]
    
    for x in solution: # [1,2,3]
        if all(y in player_pos[cur_player] for y in x): # 1 -> 2 -> 3
            # if any winning combination satisfies, return true
            return "Win"

    return False 

def single_game(cur_player):
    inputs = []
    for x in range(9):
        inputs.append(' ')

    player_pos = {'X':[], 'O':[]}
    while True:
        grid_tic_tac_toe(inputs)

        # Get Move Input
        print("Player ",cur_player, " Select a grid to draw(select from 1 to 9): ", end="")
        move = int(input()) # 1~9 
          
        # Sanity Check
        if move < 1 or move > 9:
            print("❌Wrong input type again❌")
            continue

        # Check if the box is already occupied
        if inputs[move-1] != ' ':
            print("❌grid already taken. Try again❌")
            continue
        
        # Upadte grid status
        inputs[move-1] = cur_player
        player_pos[cur_player].append(move)
        
        # Function call for check_win
        if check_status(player_pos, cur_player) == "Win":
            grid_tic_tac_toe(inputs)
            print("Player ",cur_player, " won!🎉 \n")
            return cur_player

        if check_status(player_pos, cur_player) == "Draw":
            grid_tic_tac_toe(inputs)
            print("Game Drawn \n")
            return "Drawn"
        
        # switch player
        if cur_player == 'X':
            cur_player = 'O'
        else:
            cur_player = 'X'


    # stores the positions of X and O

# main 
player1 = "X"
player2 = "O"

cur_player = player1
player_choice = {'X' : "", 'O': ""}

while True:
    player_choice['X'] = cur_player
    if cur_player == player1:
        player_choice['O'] = player2
    else:
        player_choice['O'] = player1 
    
    single_game('X')

    if cur_player == player1:
        cur_player = player2
    else:
        cur_player = player1 

# streos the choice of players



    
