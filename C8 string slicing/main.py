#string Slicing ~ create a substring by extracting elements from another string.
       
#      indexing[] or slicing()

#      [start:stop:step]

#name="I am TamalMondal"

#first_name=name[0:10] # first parameter:second parameter

#for string slicing variable[start_index:End_Index+1] #end index meaning last point of sub string.
#here we started from 0 index and go upto 9th index , so we need to do 9+1 = 10 , which is end_point of sub string.

#print(first_name)

#---------Slicing with the third Parameter--------#

# Slicing with the third Parameter also called as step value.By default it is 1.

# Step value - 1 specifies the number of elements to skip when slicing the string....example

#name="Bro Code"

#funny_name=name[0:8:3] #here step / 3rd parameter output is B d , B space d 
#remember third parameter only work in substring or between start and stop parameter

#print(funny_name)

#Remember if you leave start and stop index empty , then start index is 0 and stop index is very end of the string.


#---------Reverse a string in Python---------#

#name="Tamal Mondal"

#reversed_name=name[::-1] #here start and stop empty because we want entire string and step -1 , its kind of like we are counting backwards.now it will create a substring based of name variable but in reverse.
#print(reversed_name)

#------------ slice() -------------#

website1= "https://w3schools.com/"
website2= "https://facebook.com/"

slice=slice(8,-5) # Every index has positive and negative value , I would like the slice to begain with index 8 and negative index of -5 for the stopping position so that will give me just the website name.

print(website1[slice])
print(website2[slice])














