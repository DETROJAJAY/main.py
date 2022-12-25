import numpy as np
# n = 20
# m = 20
arr1  = np.array(input('array1 : ').split() , dtype=int) 
arr2 = np.array(input('array2 : ').split() , dtype=int)

def sumof(arr1,arr2):
    if(len(arr1) == 0 and len(arr2) == 0 ):
        return
    elif (len(arr1) == 0 or len(arr2) == 0 ):
       return  sum(arr1) if len(arr1)>0 else sum(arr2)
    else:
        sum1 = 0
        for i in range(0 , len(arr1)):
            if arr1[i] not in arr2 :
                sum1 = sum1 + int(arr1[i])
        for j in range(0 , len(arr2)):
            if arr2[j] not in arr1:
                sum1 = sum1 + int(arr2[j])
        return sum1

print(sumof(arr1,arr2))    

