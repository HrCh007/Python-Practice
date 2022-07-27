import mymodule                    #can create an alias with as 
from mymodule import person1       #only imports person1 from mymodule and person1 can be accessed dierctly
import platform                    #In built module

x = dir(platform)
print(x)
x = platform.system()
print(x)

mymodule.greeting("Jonathan")

a = mymodule.person1["age"]
print(a)

print (person1["age"])             #possible due to from keyword

