from functools import wraps

def deco(f):
    @wraps(f)
    def rp(*a ,  **k):
        '''this is wrapper function'''
        print("this is awsome")
        return f(*a , **k)
    return rp

@deco
def fun1(a):
    '''this is just function'''
    print(f"this is fuction with argument {a}")

# j = deco(fun1)
# j()

fun1(7)
print(fun1.__doc__)


#***********************************************************************************************#
print("\n")
#***********************************************************************************************#


def deco(z):
    @wraps(z)
    def rw(*a , **k):
        print(f'you are calling {z.__name__} function')
        print(z.__doc__)
        return z(*a , **k)
    return rw

@deco
def add(a,b):
    '''this is add function'''
    return a + b

print(add(3,2))


#***********************************************************************************************#
print("\n")
#***********************************************************************************************#


def only_type(dt):
    def deco(function):
        @wraps(function)
        def wrapper(*a ):
            if all([type(i) == dt for i in a]):
                return function(*a)
            else:
                return "ivalid input"
        return wrapper
    return deco

@only_type(int)
def add(*args):
    total = 0
    for i in args:
        total = total + i
    return total

@only_type(str)
def join(*args):
    strin = ''
    for i in args:
        strin = strin + i
    return strin

print(add(1,2,5,6, {'j' : 4}))
print(join('a' ,'d' , 's'))
