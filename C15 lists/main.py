# list = used to store multiple items in a single variable.

#food=["chicken biryani","Burger","Hotdog","Fish fry"]

#print(food)
#output: ['chicken biryani', 'Burger', 'Hotdog', 'Fish fry']

#So, if we want to access each item of the list, for that.....

# print(food[0])
#output: chicken biryani
# so here we are using index number to access each list item.

# Now we want to access all the list item without square brackets

# for i in food:
#     print(i)
#output:
# chicken biryani
# Burger
# Hotdog
# Fish fry

#-------- some more useful function of list -------#

#food=["chicken biryani","Burger","Hotdog","Fish fry"]

#---------if we want to change a list item for that....

# food[1]="Pizza"
# print(food)
# output : ['chicken biryani', 'Pizza', 'Hotdog', 'Fish fry']
# so we are successfully changed index 1 str value.


#--------if we want to append a list item to the end of the list--------#

# food.append("lassi")
# print(food)
# output: ['chicken biryani', 'Burger', 'Hotdog', 'Fish fry', 'lassi']
# so we successfully append a new item in the list.


#-----------if we want to remove a item---------#

# food.remove("Burger")
# print(food)

#output: ['chicken biryani', 'Hotdog', 'Fish fry']
# so we successfully removed a list item from the list.


#-------if we want to remove last item of the list-------#

# food.pop()
# print(food)

#output: ['chicken biryani', 'Burger', 'Hotdog']
# so we successfully removed last item from the list using pop() function.


#---------if we want to insert a new item----------#

# food.insert(3,"Egg roll")
# print(food)

#output: ['chicken biryani', 'Burger', 'Hotdog', 'Egg roll', 'Fish fry']
# so here we insert a item in list index 3 #interesting thing is that new item take index 3 position and shift previous index 3 item to index 4.

#-------if i want to sort in alphabetical order--------#

# food.sort()
# print(food)

#output: ['Burger', 'Fish fry', 'Hotdog', 'chicken biryani']
#now list is in alphabetical order


#------------- if we want to clear all the list item from the list ----------#

# food.clear()
# print(food)

#output: []
# so that's how we clear all the item from the list.