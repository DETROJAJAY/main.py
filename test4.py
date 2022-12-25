import numpy as np

def productt(ary):
    for i in range(0 , len(ary)):
        print(((np.prod([i for i in ary]))/ary[i]) , end="  ")
    

j = np.array(input('array1 : ').split() , dtype=int)
productt(j)