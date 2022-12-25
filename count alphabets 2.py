jay= input("input the number: ")
i = 0
extra = ''
while i < len(jay):
    if jay[i] not in extra:
        print(jay[i] ,"=", jay.count(jay[i]))
        extra = extra + jay[i]
        i = i+1
    else:
        i = i + 1
