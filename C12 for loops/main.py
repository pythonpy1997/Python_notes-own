# for loop= a statement that will execute a block of code a limited amount of time.

#               while loop = unlimited
#               for loop = limied


#-------Introduction to range() Function------#

#Returns a series of numbers.

# range(start,stop,step)

#starting position of the sequence , default value is 0

#stopping position of the sequence.never included in the result of the range() function

#step = Specifies the increment value.default value 1
#it means if the step is 2 and start is 0 then 0+2 give us 2 step value and then 2+2 = 4 is step value.


#-----------for loop with range(start,stop)----------#

# Generates a sequence of intergers starting from start to stop-1.

# for i in range(0,20):
#     print(i)
# print("Done!")    


#--------for loop with range(start,stop,step)--------#

#Generates a sequence of integers starting from "start", incremented by "step" , and stopped at "stop"-1

# for i in range(1,10,2):
#     print(i)
# print("done!")   

# range() function only works with integer arguments.
#All three arguments can be positive or negative.
#step value cannot be zero thats why default step value is 1.

# for i in "Tamal":
#     print(i)

import time
for sec in range(10,0,-1):
    print(sec)
    time.sleep(1)
print("Happy New Year")    
