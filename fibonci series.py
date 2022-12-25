def jay(a):
    i = 1
    x = 1
    z = 0
    y = 0
    while i <= a:
            print(z, end = ",")
            z = x + y
            x = y
            y = z
            i = i + 1
    
        
    
a = int(input("enter the number of series"))
(jay(a))
