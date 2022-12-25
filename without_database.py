a = 'yes'
x,p,z = 0,0,2
y = []
while a == 'yes':

   j = {
    'surname' : input("enter your surname: ")
      }

   j['name'] = input('input your name: ')
   j["age"] = input('input your age: ')
   j["movies"] = list(input("input list of you favourit movie: ").split(","))
   j["songs"] = list(input("input list of you favourit songs: ").split(","))
   y.append(j)
   
   a = input(f"do you want to enter{z} persone's detelis; yes or no: ")
for a in y:
   for i,j in a.items():
      if p == x:
         x = x + 1
         print("person: " + str(x))
      print(F"\t{i} : {j}")
   p = p +1
