
name = input("enter the strings\n")
ll = []
i = 0
j = 0
for j in name:
    j = name[i]
    ll.append(j)
    i = i+1

l1 = []
q = 0
r = 0
for q in ll:
    q = ll[r]
    if q not in l1:
        l1.append(q)
    r = r + 1

t = len(l1)
p = 0
while int(p) < int(t):
    g = l1[p]
    a = ll.count(g)
    print(l1[p],"=",a)
    p = p + 1
