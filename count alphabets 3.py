def jay(a):
    d = {}
    for i in a:
        d[i] = a.count(i)
    return d



print(jay(input("enter a number")))