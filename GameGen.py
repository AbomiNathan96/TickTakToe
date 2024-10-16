def removeD(S):
    R = True
    for i in range(9):# removes it if it has twice of the same digit in the number
        if S.find(str(i)) != S.rfind(str(i)):
            R = False
    return R

with open('out.txt','w') as f:
    for I in range(888888889):
        i = I
        S = str(i)
        for i in range(9-len(S)):#counts up to 888888888889 and removes 9
            S = '0' + S
        if S.find('9') == -1 and removeD(S) == True:
            f.write(S+'\n')
        
