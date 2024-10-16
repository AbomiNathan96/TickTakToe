
def checkwin(G):# code to see if you won
    Game = 0
    I = 1
    if G[0:3] == [I,I,I] or G[3:6] == [I,I,I] or G[6:9] == [I,I,I] or [G[0],G[3],G[6]] == [I,I,I] or [G[1],G[4],G[7]] == [I,I,I] or [G[2],G[5],G[8]] == [I,I,I] or [G[0],G[4],G[8]] == [I,I,I] or [G[2],G[4],G[6]] == [I,I,I]:
        Game = 1
    I = 2
    if G[0:3] == [I,I,I] or G[3:6] == [I,I,I] or G[6:9] == [I,I,I] or [G[0],G[3],G[6]] == [I,I,I] or [G[1],G[4],G[7]] == [I,I,I] or [G[2],G[5],G[8]] == [I,I,I] or [G[0],G[4],G[8]] == [I,I,I] or [G[2],G[4],G[6]] == [I,I,I]:
        Game = 2
    return(Game)

f = open('games.txt')
Lines = f.readlines()#reads all of the games
f.close()

with open('outcomes.txt','w') as f:
    for line in Lines:
        G = [0,0,0,0,0,0,0,0,0]
        R = 0
        for I in range(9):
            if round(I/2) == I/2:#odd or even
                G[int(line[I])] = 1# decides the outcome of the game
            else:
                G[int(line[I])] = 2
            if R == 0:
                R = checkwin(G)
        f.write(str(R)+'\n')#write it down
                
                
