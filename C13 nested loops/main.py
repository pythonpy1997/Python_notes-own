


# for j in range(0,4,1):
#     print("#")

#output like this #
                  #
                  #
                  #
    
# ok , now we want # should not go to next line , we want them horizontal of each other , for that.....
    
#for j in range(0,4,1):
        #print("#",end=" ")

#output like this # # # #

# ok , here we used end 
#        What is Python End Parameter?
        
# ANS: For the addition of any string at the end of the python print statement output, we use the python end Parameter. The print function in python by default ends with a new line. If the whitespace is passed to the end Parameter (end=' ') then it shows that not the new line but the whitespace will be used to identify the end character. There is always a creation of a newline by the print() function of python. Instead of newline we can also add some other characters at the end of the print statement by using end in python. 

        
#ok ,  Now we want a square .....      

# for j in range(0,4,1):
#         print("#",end=" ")

# for j in range(0,4,1):
#         print("#",end=" ")

# for j in range(0,4,1):
#         print("#",end=" ")

# output like this # # # # # # # # # # # # 

# so now we want new line after every four # 
# or we need new line after every for loop , for that 
        
# for j in range(0,4,1):
#         print("#",end=" ")

# print()

# for j in range(0,4,1):
#         print("#",end=" ")
# print()

# for j in range(0,4,1):
#         print("#",end=" ")    

# print()

# output like this... 
# # # # 
# # # # 
# # # # 

# ok , now its looks fine but , we need to write too much for loop for that , so here we will use nested loops which is besically , Inside one loop there is another loop.

# for i in range (0,5,1):
#         for j in range(0,4,1):
#                 print("#",end=" ")

#         print()
# output be like 
        
# # # # 
# # # # 
# # # # 
# # # # 
# # # #         
        
# ok so here , we used nested loop and outer loop [i] run 5 times and print inner loop 5 times in new line becuse we used print() for new line inside inner loop and 
#if You dont know remember print() always go to new line.
        

# Now we will create a triangle using nested loop...
        
# we want 8 line of triangle

# for i in range(8):
#         for j in range(i):
#                 print("#", end=" ")
#         print()        

# output be like 

# 
# # 
# # # 
# # # # 
# # # # # 
# # # # # # 
# # # # # # # 

# so here , we are using value of i from outer loop to inner loop and then value of i will be 1 , it will print one # , when value of i will be 2 then two # like this 
        # but interesting thing is we have only seven line , because value of i starts from 0 ....so for that , 

# for i in range(8):
#         for j in range(i+1):
#              print("#",end=" ")
#         print()

# now output is 
# 
# # 
# # # 
# # # # 
# # # # # 
# # # # # # 
# # # # # # # 
# # # # # # # # 

# Now we have 8 lines because we add (i+1) in inner loop , so 0+1=1 , and so now first value of i will be 1.
                

 #--------reverse triangle----------#

for i in range(4):
       for j in range(4-i):
            print("#",end=" ")
       print()  

# output is
# # # # 
# # # 
# # 
# 

#so here in reverse triangle , we take inner loop (4-i) , its like when i value is 0 then j value will be 4 , when i value is 1 then j value will be 3 .... and thats how it will print new value every line and value of j decrease in every line so we will get a reverse tri angle.                                 