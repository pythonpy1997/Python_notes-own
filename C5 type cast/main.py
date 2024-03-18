# #type casting= convert the data type of a value to another data type.

# x=2 #int
# y=3.0 #float
# z="4" #str

# x=float(x) #type casted x , int to float

# y=int(y) # here we type cast y float to int with permanent change , now y is whole integer

# z=int(z)

# print(x) 

# #print(y)
# #print(int(y)) #here we type cast float to int ,but its not permanent change , for that...
# print(y) 

# #print(z)
# print(z*4) # whats happening here is , printing 4 four times , because z="4" and "4" is str . now .... we gave z=int(z) in line 9 , now z act like int because we type cast it , str to and result is 4.

#when we need change int/float to a string ??

# x=2 #int
# y=3.0 #float
# z="4" #str

#print("X is: "+x) # You cant normally display float / int along side with str , because we are using string concatenation.
#print("Y is: "+y)

# print("X is: "+str(x))
# print ("Y is: "+str(y))
