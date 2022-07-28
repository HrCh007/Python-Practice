import os                              # for deleting files

f = open("dfile.txt", "r")
print(f.read())
f.close() 

f = open("dfile.txt", "r")
print(f.read(5))                        # returns the first 5 characters from the file
f.close() 

f = open("dfile.txt", "r")
print(f.readline())                     # returns a single line
print(f.readline())
f.close()   

f = open("dfile.txt", "r")
for x in f:                             # loop throuh the file line by line
  print(x)
f.close()                               # good practice to always close the file when done with it


f = open("dfile2.txt", "a")                           # 'a' for appending to the end of the file
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:

f = open("dfile2.txt", "r")
print(f.read())
f.close()   

f = open("dfile3.txt", "w")                            # 'w' for overwriting the existing file
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("dfile3.txt", "r")
print(f.read())

# f = open("myfile.txt", "x")                          # 'x' to create a file called "myfile.txt" (gives error if the file already exists)

f = open("myfile.txt", "w")                          # Create a new file if it does not exist


if os.path.exists("demofile.txt"):                   # checks if the file exists
  os.remove("demofile.txt")                          # deletes the file (gives error if the file does not exist)
else:
  print("The file does not exist")

# os.rmdir("myfolder")                               # to remove an empty folder (gives error if the folder does not exist)