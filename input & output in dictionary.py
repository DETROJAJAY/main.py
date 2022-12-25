def jay(**a):
  
   p = 0
   z = list(a.values())
   x = 0
   while p < len(z[0]):
      for i,j in a.items():
         if p == x:
            x = x + 1
            print("person: " + str(x))
            
         print(F"\t{i} : {j[p]}")
      p = p +1
      
      
jay(name = list(input("enter the names : ").split(",")), age = list(input("enter the ages : ").split(',')))