from random import randint, random
j = randint(0,100)
a = int(input("guass the number between 0 to 100 : "))
i = 1
if a != j:
    while a != j:
        if a > j:
            print("you guassed wrong...too high")
        else:
            print("you guassed wrong...too low")
        i = i + 1
        a = int(input('guaass again : '))

print("right!!!......you guass this number in",i, "attemed ")