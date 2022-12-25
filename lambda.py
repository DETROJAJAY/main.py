num = [1,4,8,2,9,4]
name = ['jay','heet','dishant']

a = lambda a,b : [pos for pos,target in enumerate(a) if b == target] if  any([(b == target) for pos,target in enumerate(a)]) else "not in list"

print(a(name ,'meet'))