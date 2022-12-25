for i in range(1 , 6):
    for j in range (0 , i):
        print(i,end="")
    print(" ")

for i in range(1,5):
    for j in range(0,6):
        print(i,end="")
    print(" ")

for i in range(0,6):
    j = 6
    while ( j > i):
        print(i,end="")
        j = j - 1
    print('')

for i in range(0,6):
    j = 6
    while ( j > i):
        print(' ',end='')
        j = j - 1
    print(i)

for i in range(0 , 6):
    for j in range (0, i):
        print(" ",end = '')
    print(i)
    
for i in range(1,6):
    for j in range(5,i,-1):
        print(' ',end='')
    for z in range(0,i):
        print(i,end='')
    print('')

# for i in range(5,0,-1):
#     print(' ',end='')
#     for j in range(i,0,-1):
#         print(i)
    