j = {
    'surname' : input("enter your surname: ")
}

j['name'] = input('input your name: ')
j["age"] = input('input your age: ')
j["movies"] = list(input("input list of you favourit movie: ").split(","))
j["songs"] = list(input("input list of you favourit songs: ").split(","))

def jay(a):
    for key,value in a.items():
        print(key ,":", value)

jay(j)