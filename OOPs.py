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
class shape:
    def area(self):
        raise NotImplementedError("Subclass Must implement the abstract methods")

class Square(shape):
    def __init__(self,l):
        self.l=l

    def area(self):
        print("Area of square is ",self.l*self.l)

class Rect(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    def area(self):
        print("Area of Rect is ",self.l*self.b)

obj_sq=Square(10)
obj_rec=Rect(10,8)

for obj in (obj_sq,obj_rec):
    obj.area()



#Inheritance

# parent class
class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def display(self):
    print(self.name, self.age)

# child class
class Student(Person):
  def __init__(self, name, age):
    self.sName = name
    self.sAge = age
    # inheriting the properties of parent class
    super().__init__("Rajeev", age)

  def displayInfo(self):
    print(self.sName, self.sAge)

obj = Student("Rajeev", 23)
obj.display()
obj.displayInfo()
