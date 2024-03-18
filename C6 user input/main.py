name=input("What's your name?: ")

age=int(input("How old are you: ")) #when we use str in any kind of mathmatical calculation , then we need to type cast it into int/float

height=float(input("How tall are you?: "))

print("Hello "+name)

print("You are "+str(age)+" years old") #if we give decimal value then we will face value error : ValueError: invalid literal for int()

print("Ok , You are "+str(height)+" ft. tall")

