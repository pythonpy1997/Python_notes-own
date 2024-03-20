#Logical operators (and,or,not) = use to check if two or more conditional statement.

#------------logical operator "and"-------------#

temp= int(input("What's the current temperature outside?: "))

#if temp>=0 and temp<=30: # In logical operator "and" , both condition must be true in order for the statement to be true.
    #print("Looks like , Temperature is good today!")
    #print("Go outside!")


#--------------- "or" logical operator--------------#

#if temp>=0 and temp<=30:
   # print("Weather pretty good outside , go outside")
#elif temp<0 or temp>30: #In "or" logical operator as long as one condition is true then the entire statement is true.It does not matter one of them is false , just need one condition to be true.
   # print("Weather ouside very bad , stay inside")



#--------------- "not" logical operator--------------#
    
# if not(temp>=0 and temp<=30):
#     print("Weather pretty good outside , go outside")
# elif not(temp<0 or temp>30): 
#     print("Weather ouside very bad , stay inside")    

#so with not logical operator we can surround one or more conditional statements with not logical operator and what not logical operator do is flip it from being false to true or from true to false.
    
#here we can change print message for both condition to get right output with not logical operator ..... like this     

if not(temp>=0 and temp<=30):
   print("Weather ouside very bad , stay inside")  
elif not(temp<0 or temp>30): 
    print("Weather pretty good outside , go outside")