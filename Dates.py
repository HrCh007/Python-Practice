import datetime

x = datetime.datetime.now()
print(x)

x = datetime.datetime(2020, 5, 17)
print(x)
print(type(x))

#strftime formats date objects into readable strings
                                  
print(x.strftime("%B"))              #strftime takes one pararmeter ie. format (refer to w3schools for various formats)