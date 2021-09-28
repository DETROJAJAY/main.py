j = input("Please enter a string")
def mf(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
             d[key] += 1

    return d
print(mf(j))