#Python Classes and Objects

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):              #__init__() function is called automatically when a new object is created.
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

p1.age = 40
print(p1.age)

del p1.age

del p1