# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# Function that checks if a given play was won the game
def check_win(l_play):

    min_choice = min(l_play) #minimal number of chosen ones
    max_choice = max(l_play) #max number of chosen ones

    if len(l_play) < 3: #in case that less than 3 numbers were chosen yet
        return False
    elif(min_choice == 5 or min_choice == 6 or min_choice == 8 or min_choice == 9): #combinations that don't win the game
        return False
    elif(max_choice == 1 or max_choice == 2 or max_choice == 4 or max_choice == 5): #combinations that don't win the game
        return False
    elif(1 in l_play and ((2 in l_play and 3 in l_play) or (4 in l_play and 7 in l_play) or (5 in l_play and 9 in l_play))):
        return True
    elif(2 in l_play and ((5 in l_play and 8 in l_play))):
        return True
    elif(3 in l_play and ((6 in l_play and 9 in l_play) or (5 in l_play and 7 in l_play))):
        return True
    elif(4 in l_play and ((5 in l_play and 6 in l_play))):
        return True
    elif(7 in l_play and ((8 in l_play and 9 in l_play))):
        return True

def print_grid(selections):
    print(" {} | {} | {} ".format(selections[0], selections[1], selections[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(selections[3], selections[4], selections[5]))
    print("---+---+---")
    print(" {} | {} | {} \n".format(selections[6], selections[7], selections[8]))