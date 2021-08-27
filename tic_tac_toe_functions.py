# ---------------------------------------------------------------------------------------------------------------------------------------------------------
# Function that checks if a given play was won the game
def check_win(l_play):

    min_choice = min(l_play) #minimal number of chosen ones

    if len(l_play) < 3: #caso ainda não tenha três números
        return False
    elif(min_choice == 5 or min_choice == 6 or min_choice == 8 or min_choice == 9): #combinations that don't win the game
        return False
    elif(min_choice == 1 and ((2 in l_play and 3 in l_play) or (4 in l_play and 7 in l_play) or (5 in l_play and 9 in l_play))):
        return True
    elif(min_choice == 2 and ((5 in l_play and 8 in l_play))):
        return True
    elif(min_choice == 3 and ((6 in l_play and 9 in l_play) or (5 in l_play and 7 in l_play))):
        return True
    elif(min_choice == 4 and ((5 in l_play and 6 in l_play))):
        return True
    elif(min_choice == 7 and ((8 in l_play and 9 in l_play))):
        return True

def print_grid(selections):
    print(" {} | {} | {} ".format(selections[0], selections[1], selections[2]))
    print("---+---+---")
    print(" {} | {} | {} ".format(selections[3], selections[4], selections[5]))
    print("---+---+---")
    print(" {} | {} | {} \n".format(selections[6], selections[7], selections[8]))