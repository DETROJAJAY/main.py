def comm(a,b,c):
    x = [p for p in a]
    y = [q for q in b]
    z = [r for r in c]
    new = []
    for i in x:
        if i in y and z:
            new.append(i)
    return new if len(new)>0 else -1

a = input('a : ')
b = input('b: ')
c = input('c: ')
print(comm(a,b,c))