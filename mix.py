def jay(*names,revers_str = 'unknow'):
   print([(a[::-1]).title() for a in names] if revers_str == 'true' else [a.title() for a in names])
   

jay(*(list(input('enter the names: ').split(','))),revers_str=input('true or false: '))
