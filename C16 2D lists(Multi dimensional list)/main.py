# 2D list or Multi dimensional lists = a list of lists

drinks=["coffee","lassi","tea"]
dinner=["chicken-soup","rice","daal"]
dessert=["sweet","ice cream"]

food=[drinks,dinner,dessert] #This is a 2D list
#print(food)

#output : [['coffee', 'lassi', 'tea'], ['chicken soup', 'rice', 'daal'], ['sweet', 'ice cream']]

# so whats happening is , this will print all of the elements found within each individual list and they are all grouped together.
#the first portion is my drink list which contains coffee , lassi and tea and 2nd and 3rd portion same as 1st portion. 


#------so if i need to acess just one of these lists i will add index after my food 2D list-------#

# print(food[0])
# so index zero is refering to my first list of drink and it will display all the elements found within my first list.
#if i need one the element , i will add......

# print(food[0][1])
#output:lassi

#print(food[1][2])
#output: daal
# so here we are working with a different list this time we are working with our dinner list.

# print(food[2][2]) 

# so here we are getting "IndexError: list index out of range" error because we only have two value within this list sweet and ice cream. There is no element at index 2 because we only added 2 elements to this list of dessert.


