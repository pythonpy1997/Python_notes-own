# set = collection which is unordered , unindexed. No duplicate values.

# utensils={"fork","spoon","knife"}

# for x in utensils:
#     print(x)

#every time we run set , order of set elements different
# set is faster than list
    
# utensils={"fork","spoon","knife","knife","knife"}

# for x in utensils:
#     print(x)

 #output:
# knife
# spoon
# fork 

#here we have 3 knifes but only diplayed just one , because set do not allow any duplicate value.


#---------- few useful methods of set ----------#

# utensils={"fork","spoon","knife"}
# dishes={"bowl","cup","plate"}

#utensils.add("napkin") # thats how we can add a element within set

#utensils.remove("fork") # thats how we can remove a element from set

#utensils.clear() #All the element from the utensils gone now.



# now we are going to add one set to another set using the update method 
# lets say , we like to add our dishes set to our utensils set ,.....for that

#utensils.update(dishes)
#output: 
# plate
# fork
# bowl
# knife
# cup
# spoon

#we are successfully added dishes set to utensils set.

# for x in utensils:
#      print(x)


# lets create a set called dinner table , like we are setting a dinner table , we need a bowl , plate , knife , spoon , fork , cup
#                   for that,

# dinner_table=utensils.union(dishes)

# for i in dinner_table:
#     print(i)

# output : 
# fork
# spoon
# bowl
# plate
# cup
# knife


# if we want to see differences between two sets , exp.
# i would like to see what utensils has and dishes doesn't , for that we will use difference method.

utensils={"fork","spoon","knife"}
dishes={"bowl","cup","plate","knife"}

#print(utensils.difference(dishes))

#output: 
#{'spoon', 'fork'}
# this will print what utensils has and dishes doesn't
# we can reverse the roles too

#print(dishes.difference(utensils))
 
#output: 
#{'bowl', 'cup', 'plate'}

# they both have knife so knife doesn't appearing



#------- we can also check to see is there anything they have in common using intersection method------#

#print(utensils.intersection(dishes)) 

# this will return what ever they have common , which is knife 

#output: 
#{'knife'}

