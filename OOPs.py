# class Info:
#     def __init__(self, n, c):
#         self.n = n
#         self.c = c

#     def __init__(something,n,a):
#         something.n=n
#         something.a=a

#     def show(self):
#         print("Hello my name is " + self.n+" and I" +
#               " work in "+self.c+" And My Age is ."+ self.a)
    
#     def show1(self):
#         print("Hello my name is " + self.n+" And My Age is ",self.a)


# obj = Info("Rajeev", "OC")
# obj1= Info("Rajeev",23)
# obj1.show1()

#Polymorphism and Inheritance
# class shape:
#     def area(self):
#         raise NotImplementedError("Subclass Must implement the abstract methods")

# class Square(shape):
#     def __init__(self,l):
#         self.l=l

#     def area(self):
#         print("Area of square is ",self.l*self.l)

# class Rect(shape):
#     def __init__(self,l,b):
#         self.l=l
#         self.b=b
    
#     def area(self):
#         print("Area of Rect is ",self.l*self.b)

# obj_sq=Square(10)
# obj_rec=Rect(10,8)

# for obj in (obj_sq,obj_rec):
#     obj.area()



# #Inheritance

# # parent class
# class Person():
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def display(self):
#     print(self.name, self.age)

# # child class
# class Student(Person):
#   def __init__(self, name, age):
#     self.sName = name
#     self.sAge = age
#     # inheriting the properties of parent class
#     super().__init__("Rajeev", age)
 
#   def displayInfo(self):
#     print(self.sName, self.sAge)

# obj = Student("Rajeev", 23)
# obj.display()
# obj.displayInfo()

# # Python program to demonstrate private members
# # of the parent class

# class C(object):
#     def __init__(self):
#         self.c = 21

#         # d is private instance variable
#         self.__d = 42


# class D(C):
#     def __init__(self):
#         self.e = 84
#         C.__init__(self)

# object1 = D()

# # produces an error as d is private instance variable
# print(object1.c)
# print(object1.__d)


#Abstraction

from abc import ABC

class R(ABC):
    def rk(self):
        print("Abstract Base Class")

class K(R):
    def rk(self):
        super().rk()# invoking method of super class
        print("subclass ")

# Driver code
r = K()
r.rk()

#Abstract class cannot be instantiated

from abc import ABC,abstractmethod

class S(ABC):
   @abstractmethod
   def fun(self):
      pass

class C(S):
   def fun(self):
      print("Implemented fun in child class")

try:
    ob=S()
except Exception as err:
    print(err)

ob1=C()
ob1.fun()

#Iterators

# Iterating over a list
print("List Iteration")
l = ["Hello", "World"]
for i in l:
	print(i)
	
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("Hello ", "World", "Tuples")
for i in t:
	print(i)
	
# Iterating over a String
print("\nString Iteration") 
s = "World"
for i in s :
	print(i)
	
# Iterating over dictionary
print("\nDictionary Iteration") 
d = dict() 
d['xyz'] = 123
d['abc'] = 345
for i in d :
	print("%s %d" %(i, d[i]))
