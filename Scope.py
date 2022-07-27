#Scope of variables

x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

#Global Keyword

def myfunc():
  global x
  x = 300

myfunc()

print(x)

#use global keyword to change global variable inside a function

x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)
