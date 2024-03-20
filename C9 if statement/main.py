#if statement = a block of code that will execute if its condition is true.

age=int(input("How old are you?: "))

#---------------- if statement ------------#

# if age>=18:
#     print("You are an adult!")
# else:
#     print("You are a child!")

#---------------else if statement----------#

# if age>=18:
#     print("You are an adult")
# elif age<0:
#     print("You haven't been born yet")
# else:
#     print("You are a child")



# if age>=18:
#     print("You are an adult")
# elif age==100:
#     print("You are century old")
# elif age<0:
#     print("You haven't been born yet")
# else:
#     print("You are a child")

#     Btw it's a broken code or faulty code , because if we give 100 year , the first condition will execute and output will be "you are an adult" and it will skip whole other conditions and age==100 never execute....to fix this problem...


if age==100: # "==" this is comparison operator for equality , but if you use just "=" that's assignment operator , and python think you want to set age equal to 100. so if you want to see age equal to 100 then use double equals.
 print("you are century old")
elif age>=18:
    print("You are an adult")
elif age<0:
    print("You haven't been born yet")
else:
    print("You are a child")

# So now code is working because order of your if statement does matter , so first we will check ageequal to 100 or not if not then age equal or greater than 18 or not ... and rest of the condition run same way until we reach else statement.    
    