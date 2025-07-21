import os
clear = lambda: os.system('cls')


def display(G): #this is the code for displaying the board and checking for wins
    #clear()
    R = 0
    for I in range(9-len(G)):
        G = G + " " #makes sure its 9 char long
    out = [' .',' .',' .',' .',' .',' .',' .',' .',' .']
    out2 = [0,0,0,0,0,0,0,0,0]
    for I in range(9):
        if G[I] != ' ':
            if round(I/2) == I/2:
                out[int(G[I])] = ' X'
                out2[int(G[I])] = 1 # this converts for checking
            else:
                out[int(G[I])] = ' O'
                out2[int(G[I])] = 2
            if R == 0:
                R = checkwin(out2) # if a fate hasent been decided yet it deciedes
    print(out[0]+out[1]+out[2]+'  0 1 2\n'+out[3]+out[4]+out[5]+'  3 4 5\n'+out[6]+out[7]+out[8]+'  6 7 8\n') 
    return R

def checkwin(G): #this is the code for checking a outcomes, I hate it
    Game = 0 # 0 = stalemate, 1 = outcomes, 2 = lose
    I = 1
    if G[0:3] == [I,I,I] or G[3:6] == [I,I,I] or G[6:9] == [I,I,I] or [G[0],G[3],G[6]] == [I,I,I] or [G[1],G[4],G[7]] == [I,I,I] or [G[2],G[5],G[8]] == [I,I,I] or [G[0],G[4],G[8]] == [I,I,I] or [G[2],G[4],G[6]] == [I,I,I]:
        Game = 1
    I = 2
    if G[0:3] == [I,I,I] or G[3:6] == [I,I,I] or G[6:9] == [I,I,I] or [G[0],G[3],G[6]] == [I,I,I] or [G[1],G[4],G[7]] == [I,I,I] or [G[2],G[5],G[8]] == [I,I,I] or [G[0],G[4],G[8]] == [I,I,I] or [G[2],G[4],G[6]] == [I,I,I]:
        Game = 2
    return(Game)

def PLAYGAME():#to reaply a game
    f = open('games.txt')
    Games = f.readlines()# theese are the games i stored
    f.close()
    
    f = open('outcomes.txt')# theses are the outcomes of the games
    outcomes = f.readlines()
    f.close()
    
    Game = ""#🕶
    Turn = 0#🕶 # the coolest variable setup you have ever seen
    Playing = 0#🕶
    
    Playing = display(Game) #this spawns the ...'s
    while Playing == 0 and Turn < 9:# this ends the game
        
        Game += input()# litterally all of the code for your turn
        Turn = Turn + 1
        Playing = display(Game)
        #you ^ vs the guy she tells you not to worry about v
    
        temp = []
        temp2 = []
        for I in range(len(Games)):
            if Games[I][0:Turn] == Game:
                temp = temp + [Games[I]] #this trims the selection of games to only allow the ones that branch off the current one
                temp2 = temp2 + [outcomes[I]]
        Games = temp
        outcomes = temp2
    
    
    
        Wins = []# this is for mem stuff
        for i in range(9):
            WL = [0,1,0,0]
            for I in range(len(Games)):
                if Games[I][Turn] == str(i):
                    WL[3] = Games[I][Turn]
                    if int(outcomes[I]) == 2:
                        WL[0] = WL[0]+1
                    elif int(outcomes[I]) == 1:#this part counts all the wins losses and stalemates that could happen
                        WL[1] = WL[1]+1
                    elif int(outcomes[I]) == 0:
                        WL[2] = WL[2]+1
    
            if WL[0] == 0:
                print(WL[0],WL[1],WL[2],WL[2]/WL[1],WL[3]) #if there are no ways to outcomes, treat a stalemate as a outcomes
                Wins += [WL[2]+WL[0]]
            else:
                print(WL[0],WL[1],WL[2],WL[0]/(WL[1]*2),WL[3])
                Wins += [WL[2]+WL[0]]
    
    
    
        temp = []
        for wow in range(9):
            temp = temp + [Wins[wow]] # this part copys the Wins list, but if i did temp = Wins, the they would refrence the same object so when i sorted it with .sort() both would have been sorted
        temp.sort(reverse=True) 
        EGG = 0
        EG = ''
    
        for i in Wins:
            if temp[0] == i:
                EG = str(EGG)
                break # this part chooses the best move
            EGG += 1
        if temp[0] != 0:# i  need this so that when all moves suck it wont just steal the 0 spot
            Game = Game + EG
    
        Turn += 1
        Playing = display(Game)
    
    display(Game)
    
    
    match Playing:
        case 0:
            print("Stalemate!")
        case 2:
            print("Lose!") #prints the end of the game
        case 1:
            print("Win!")
    if (input('\n\n Replay? Y/N').lower() == 'y' ):
        print('\nhave "fun"\n')
        PLAYGAME()
    else:
        print('\n\n\nyou made the right choice')
        return "its finnaly over"


print("Soz m8 dev here, due to a bug you can steal the bot's spaces so... dont\n\n")
PLAYGAME() #LET THE GAMES....    BEGIN!
