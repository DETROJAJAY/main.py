def addposition(a,b):
    if pos[a] in  ('O','X'):
        print('the position is not empty')
        if b == 'O':
            pyr1()
        else:
            pyr2()
    else:
        pos[a] = f'{b}'
        print(pos[0:3])
        print(pos[3:6])
        print(pos[6:9])
        for i,j,k in ((0,1,2),(0,3,6),(3,4,5),(6,7,8),(1,4,7),(2,5,8),(0,4,8),(2,4,7)):
                if pos[i] == pos[j] == pos[k]:
                    if pos[i]=='O':
                        print('player 1 Win')
                        return 'false'
                    else:
                        print('player 2 Win')
                        return 'false'
    return 'true'

def pyr1():
    player1 = int(input("enter the location,player 1: "))
    z = addposition(player1,'O')
    return z

def pyr2():
    player2 = int(input("enter the location,player 2: "))
    z = addposition(player2,'X')
    return z

def srt(a):
    if a == 'true':
        a = pyr1()
    if a == 'true':
        a = pyr2()
    if a == 'false':
        if input("do you want to play again (yes/no) : ") == 'yes':
            global pos
            pos = ['0','1','2','3','4','5','6','7','8']
            return 'true'
    return a

z = 'true'
pos = ['0','1','2','3','4','5','6','7','8']
while z == 'true':
    z = srt(z)
        
