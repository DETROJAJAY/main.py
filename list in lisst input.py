d = 1
b = []
a = "yes"
while a == 'yes':
   b.append([input(f'enter the {d} list: ')])
   a = input("do you want to enter more list; yes or no : ")
   d += 1
print(b)