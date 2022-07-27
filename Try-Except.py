# x is not defined 

try:
  print(x)
except:
  print("An exception occurred")

# The try block will generate a NameError, because x is not defined:

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

# executes else if no error is raised

try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")

#The finally block gets executed no matter if the try block raises any errors or not

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Raise an Exception

x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")