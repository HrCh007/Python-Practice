import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)       # checks if the string starts with "The" and ends with "Spain"

if x:
  print("YES! We have a match!")
else:
  print("No match")

txt = "The rain in Spain"
x = re.findall("ai", txt)         # returns a list containing all matches
print(x)

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())    

txt = "The rain in Spain"
x = re.split("\s", txt, 1)            # splits the string at first ocurence of space
print(x)

txt = "The rain in Spain"
x = re.sub("\s", "9", txt, 2)             # substitutes space with 9 for first 2 occurences of space
print(x)

x = re.search(r"\bS\w+", txt)               # regular expression looks for any words that starts with an upper case "S"
print(x.span())
print(x.string)
print(x.group())

print(type(x))        # x is a match object