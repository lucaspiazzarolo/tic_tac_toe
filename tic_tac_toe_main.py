# My first project in Python! A basic (hope so) Tic-Tac-Toe
# Let's go!

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# Import functions script
import tic_tac_toe_functions as fun

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# Request info about players
player_one = ""
player_two = ""

while player_one == "":
    player_one = input("Name of player one: ")

while player_two == "":
    player_two = input("Name of player two: ")

# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# Generating variables regarding selections and turns 

p_one_sel = [] #selections of player one (starts empty)
p_two_sel = [] #selections of player two (starts empty)
selections = ["1", "2","3", "4","5", "6", "7", "8", "9"] #all selections are, at first, empty
available = [1, 2, 3, 4, 5, 6, 7, 8, 9] #at first, all numbers are available for being chosen

p_one_turn = True #Starts with player one's turn. When it is False, it's player two's turn
valid_selection = False #shows if a selection is valid or not

game_over = False #game isn't over yet
fun.print_grid(selections) #print grid before first play
# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# Loop that will move through plays

while game_over == False:
    # ---------------------------------------------------------------------------------------------------------------------------------------------------------
    # Ask for current player input


    if p_one_turn == True: #player one's turn
        while valid_selection == False:
            try:
                selected = int(input("{}, what number is your choice? ".format(player_one)))
                if selected in available:
                    valid_selection = True
                    available.remove(selected)
                    p_one_sel.append(selected)
                    selections[selected - 1] = "X"
                    fun.print_grid(selections)

                    if fun.check_win(p_one_sel):
                        print("Congratulations, {}, you won the game!\n".format(player_one))
                        game_over = True
                        break
            except ValueError:
                continue
    else: #player two's turn
        while valid_selection == False:
            try:
                selected = int(input("{}, what number is your choice? ".format(player_two)))
                if selected in available:
                    valid_selection = True
                    available.remove(selected)
                    p_two_sel.append(selected)
                    selections[selected - 1] = "O"
                    fun.print_grid(selections)

                    if fun.check_win(p_two_sel):
                        print("Congratulations, {}, you won the game!\n".format(player_two))
                        game_over = True
                        break

            except ValueError:
                continue

    valid_selection = False
    p_one_turn = not p_one_turn
    
    if len(available) == 0: #If nobody won the game, it's a tie!
        print("Oh, it's a tie!")
        break