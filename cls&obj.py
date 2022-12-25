class Person:
    def __init__(self,name , age):
        self.first_name = name
        self.age = age  

    def bd(self):
        return f"birthdate = {2022 - (self.age)}"

    def is_ab(self):
        if self.age > 18:
            return "yes"

    def ret(self):
        return f"you entered name = {self.first_name} and age = {self.age} and is he mature? = {self.is_ab()} . so, his birthdate is {self.bd()}"


p1 = Person('jay',21)
p2 = Person('heet',20)

print(p1.ret())
print(p1.is_ab())
print(p1.bd())
print(p1.first_name)
print(p2.first_name)


#***///*****************************************************************************************\\\***#


class Leptop:
    dc = 10
    def __init__(self,name, modal_name ,price):
        self.brand_name = name
        self.modal_name = modal_name
        self.price = price
        self.price_in = f"{price/78} $"

    def apply_dc(self):
        return f"new price is {self.price - (self.price*self.dc)/100}"


Leptop.dc = 0
l1 = Leptop('lenovo','G50',45000)
l2 = Leptop('hp','bhangar',30000)
l2.dc = 30
print(l2.apply_dc())
print(l2.__dict__)
#print(l2.apply_dc(30))
print(l1.price)
print(l1.price_in)


#***///*****************************************************************************************\\\***#


class circle:
    pi = 3.14
    def __init__(self,redius):
        self.redius = redius

    def cc(self):
        return 2*circle.pi*self.redius

c = circle(3)
c1 = circle(6)
print(c.cc())


#***///*****************************************************************************************\\\***#


class Student:
    count_instance = 0
    def __init__(self , eno , name , branch):
        Student.count_instance += 1
        self.eno = eno
        self.name = name
        self.branch = branch

    @classmethod
    def frmstr(cls,str):
        ENO,NAME,BRANCH = str.split(',')
        return cls(ENO,NAME,BRANCH)

    @classmethod
    def count(cls):
        return f"you are declered {cls.count_instance} instance of {cls.__name__} class"

    @staticmethod
    def Hello():
        print("hello this is static method")


    def br(self):
        return (self.branch == 'com')

s1 = Student(7009,'jay','com')
s2 = Student(7503,'kp','mec')
s3 = Student(7525,'hi','com')
s4 = Student.frmstr("7524,he,com")

print(s4.__dict__)
print(s4.name)
print(Student.count_instance)
print(s2.br())
print(s3.__dict__)
print(Student.count())
print(Student.Hello())


#***///*****************************************************************************************\\\***#


class Phone:
    def __init__(self,brand ,modal_name,price):
        self.brand = brand
        self.modal_name = modal_name
        self._price = max(price , 0)

    @property   
    def sp(self):
        return f"{self.brand} {self.modal_name} and price : {self._price}"

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,new_price):
        self._price = max(new_price,0)


    def make_a_call(self , phone_namber):
        print(f"calling{phone_namber} ...")
    
    def full_name(self):
        return f"{self.brand} {self.modal_name}"

    def __repr__(self):
        return f"Phone('{self.brand}',{self.modal_name}',{self._price})"

    def __str__(self):
        return f"{self.brand} {self._price}"

    def __len__(self):
        return len(self.full_name())

    def __add__(self , other):
        return self._price + other._price

p1 = Phone('nokia' ,'1100',-500)
p2 = Phone('sumsang','j15',1200)
print(p1)
print(repr(p1))
print(len(p1))
print(p1 + p2)
# print(p1.__price)
# print(p1.__dict__)
# print(p1._Phone__price)
p1._price = -100
print(p1._price)
p1.price = -100
p1._price = -200
print(p1.brand)
print(p1.modal_name)
print(p1._price)
print(p1.sp)


#***///*****************************************************************************************\\\***#


class smart_phone(Phone):
    def __init__(self, brand, modal_name, price,ram,internal_memory,camera):
        super().__init__(brand, modal_name, price)
        self.ram = ram
        self.internal_memory = internal_memory
        self.camera = camera

    def full_name(self):
        return f"{self.brand} {self.modal_name} price is  {self._price}"

sp = smart_phone('redmi','note 7',9000,'3gb','32gb','12mp')

print(sp.ram)
print(sp._price)
print(sp.full_name())


#***///*****************************************************************************************\\\***#


class Flagshipphone(smart_phone):
    def __init__(self, brand, modal_name, price, ram, internal_memory, camera,front):
        super().__init__(brand, modal_name, price, ram, internal_memory, camera)
        self.front = front

    def full_name(self):
        return f"{self.brand} {self.modal_name} price is  {self._price} and cemera resolution is {self.camera}"


fp = Flagshipphone('oppo','s5',12000,'6gb','64gb','2','32mp')

print(fp.full_name())
print(isinstance(sp,Flagshipphone))
print(issubclass(Flagshipphone,smart_phone))
# print(help(smart_phone))


#***///*****************************************************************************************\\\***#


class A:

    def class_a_method(self):
        return "i m just a class A method"

    def hello(self):
        return "hello method from class A"

class B:

    def class_b_method(self):
        return "i m just a class B method"

    def hello(self):
        return "hello method from class B"

class C(A,B):
    pass

instance_c = C()
print(instance_c.class_a_method())
print(instance_c.class_b_method())
print(instance_c.hello())
print(C.mro())
print(C.__mro__)