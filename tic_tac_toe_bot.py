from termcolor import colored
import random as rd
#Defining initial values for players
pointindexX = 0
pointindexO = 0
n = 0
# ask() function works for repetition of game rounds
def ask():
    global question,n,flag_win,flag_tie
    flag_win = False
    flag_tie = False
    
    #md() allows users to choose the mode of gameplay
    def md():
        global mode
        mode = int(input("What Difficulty would you like? 1/2/3/0 \n 1 -> Bot-Easiest\n 2 -> Bot-Medium \n 3 -> Bot-Hardest \n 0 -> Multiplayer Mode\n Select Mode: "))
        if mode in [1,2,3,0]:
            play()
        else:
            print("Mode Error. Enter a possible Mode.")
            md()
    
    if n == 0:
        n +=1
        print('\n \033[1m' + colored("WELCOME TO ","blue") + colored('\033[1m' + "T","red")+colored('\033[1m' + "I","green")+colored('\033[1m' + "C","blue")+" "+colored('\033[1m' + "T","yellow")+colored('\033[1m' + "A","white")+colored('\033[1m' + "C","red")+" "+colored('\033[1m' + "T","green")+colored('\033[1m' + "O","blue")+colored('\033[1m' + "E\n","yellow"))
        md()
    elif n > 0: 
        question = input('\033[1m'+"Do you want to play again? Y/N: ").upper()
        if question == "Y":
            md()
        elif question == "N" :
            print(colored('\033[1m' + "-------------", "red"))
            print(colored('\033[1m' + "|TIC TAC TOE|", "red"))
            print(colored('\033[1m' + "-------------", "red"))
            print(colored('\033[1m' + "|FINAL SCORE|", "red"))
            print('\033[1m' + ( colored( "|","red") + colored("  X  ","green") + '\033[1m' + colored("|","red") + '\033[1m' + colored("  O  ","blue") + '\033[1m' + colored("|", "red")))
            print(colored('\033[1m' + "-------------", "red"))
            print(colored('\033[1m' + "| ","red"), '\033[1m' + colored(pointindexX,"green"),  colored('\033[1m' + " | ","red"), '\033[1m' + colored(pointindexO,"blue") , colored('\033[1m' + " |","red"))
            print(colored('\033[1m' + "-------------", "red"))
            print("\n \033[1m"+"Thanks\n")

# play() function initialises the game and allows users to play
def play():
    A = ["1","2","3","4","5","6","7","8","9"]
    player1 = colored('\033[1m' + "X", "green")
    player2 = colored('\033[1m' + "O", "blue")
    
    def board():
        print(colored('\033[1m' + "-------------", "red"))
        print(colored('\033[1m' + "|TIC TAC TOE|", "red"))
        print(colored('\033[1m' + "-------------", "red"))
        print(colored('\033[1m' + "|SCORE BOARD|", "red"))
        print('\033[1m' + ( colored( "|","red") + colored("  X  ","green") + '\033[1m' + colored("|","red") + '\033[1m' + colored("  O  ","blue") + '\033[1m' + colored("|", "red")))
        print(colored('\033[1m' + "-------------", "red"))
        print(colored('\033[1m' + "| ","red"), '\033[1m' + colored(pointindexX,"green"),  colored('\033[1m' + " | ","red"), '\033[1m' + colored(pointindexO,"blue") , colored('\033[1m' + " |","red"))
        print(colored('\033[1m' + "-------------", "red"))
        print(colored('\033[1m' + "|","red"), A[0], colored('\033[1m' + "|","red"), A[1], colored('\033[1m' +"|","red") , A[2], colored('\033[1m' +"|","red"))
        print(colored('\033[1m' + "-------------", "red"))
        print(colored('\033[1m' + "|","red"), A[3], colored('\033[1m' +"|","red"), A[4], colored('\033[1m' +"|","red") , A[5], colored('\033[1m' +"|","red"))
        print(colored('\033[1m' + "-------------", "red"))
        print(colored('\033[1m' + "|","red"), A[6], colored('\033[1m' +"|","red"), A[7], colored('\033[1m' +"|","red") , A[8], colored('\033[1m' +"|","red"))
        print(colored('\033[1m' + "-------------", "red"))
    
    #turn() function initiates turns for players to play.
    def turn(var):
        if (var == player1) or (var == player2 and mode == 0):
            move = int(input(f"Player {var}, \033[1m Enter a number from 1 to 9:"))
        elif var == player2:
            if mode == 1:
                move = mode1()
            elif mode == 2:
                move = mode2()
            elif mode == 3: 
                move = mode3()
        if A[move-1] is not player1 and A[move-1] is not player2:
            A[move-1] = var
            if (var == player1) and (mode == 0):
                board()
            elif var == player2:
                board()
        else:
            if  var == player1 or (var == player2 and mode == 0):
                print(colored('\033[1m' + "Opps! Already Occupied.\n", "red"))
            turn(var)
    
    def mode1():
        return int(rd.randint(1,9))
    
    def mode2():
        play_decision = (True,False,False)
        temp = int(rd.choice(play_decision))
        if temp == 1:
            result = mode1()
        elif temp == 0:
            result = mode3()
        return result
    
    def mode3():
        temp = None
        bot_check = [(0,1,2),(0,2,1),(1,2,0),(0,3,6),(0,6,3),(3,6,0),(0,4,8),(0,8,4),(4,8,0),(1,4,7),(1,7,4),(4,7,1),(2,5,8),(2,8,5),(5,8,2),(3,4,5),(3,5,4),(4,5,3),(6,7,8),(6,8,7),(7,8,6),(2,4,6),(2,6,4),(4,6,2)]
        test_list = ["1","2","3","4","5","6","7","8","9"]
        for i, j, k in bot_check:
            if (A[i] == A[j] == player2) and (A[k] in test_list):                
                temp = k+1
                break
        
        if temp is None:
            for i,j,k in bot_check:
                if (A[i] == A[j] == player1 and A[k] != player2) and A[i] not in test_list:
                    temp = k+1
                    break
        
        if temp is not None:
            return temp
        else:
            return mode1()
    
    #winc() is a function for defining winning conditions for the players.
    def winc(var):
        global pointindexX
        global pointindexO
        win_conditions = [(0,1,2),(0,3,6),(0,4,8),(1,4,7),(2,5,8),(3,4,5),(6,7,8),(2,4,6)]
        for i, j, k in win_conditions:
            if A[i] == A[j] == A[k] and A[i] not in ["1","2","3","4","5","6","7","8","9"]:
                if var == player1:
                    board()
                print(colored('\033[1m' + "THE WINNER IS ", "red") + A[i]+"\n")
                if A[i] is player1:
                    pointindexX +=1
                elif A[i] is player2:
                    pointindexO +=1
                return True      

    #tie() function defines ways the game might be tied.
    def tie(var):
        if all(i == player1 or i == player2 for i in A) :
            if var == player1:
                board()
            print(colored('\033[1m' + "IT IS A TIE.\n", "red"))
            return True
    
    #win() function loops to check if a player has won or not. 
    def win():
        global flag_win,flag_tie
        while flag_win is not True:
            turn(player1)
            flag_win = winc(player1)
            if flag_win is True:
                break
            else:
                flag_tie = tie(player1)
                if flag_tie is True:
                    break
                else:
                    turn(player2)
                    flag_win = winc(player2)
                    if flag_win is True:
                        break
                    else:
                        flag_tie = tie(player2)
                        if flag_tie is True:
                            break
                        else:
                            continue
        if flag_win or flag_tie is True:
            ask()
    board()
    win()

ask()