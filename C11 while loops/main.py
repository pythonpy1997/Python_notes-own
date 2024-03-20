# while loop = a statement that will execute it's block of code as long as it's condition remains true.

# name = ""

# while len(name) == 0:
#  name = input("What is your name?: ")
# here the loop run until length of the str is 0 , because its while loop.
# print("Hello "+name)



name=None

while not name:
    name=input("What is your name?: ")

print("hello "+name)

#so here name = None , None meaning empty str or false value and "not" change the value false to true . so it will run until str is empty . when str store something , condition will be true and "not" change it true to false and loop end.