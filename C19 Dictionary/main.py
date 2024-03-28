#dictionary = A changeable , unordered collection of unique key:value pairs 
#Fast because they use hashing , allow us to access a value quickly

capitals={'USA':'D.C', 'CHINA':'BEIJING','INDIA':'DELHI','RUSSIA':'MOSCOW'}

# lets say i want to print capital of russia , for that

#print(capitals['RUSSIA']) #here we used key which is associated with russia.

#print(capitals['Germany'])

#output: KeyError: 'Germany'
# My program facing a error because we used a unknown key and this will interrupt the normal flow of my program.

# A much safer way to access a key to check to see if it's there or not is to use the get method of dictionaries.

#print(capitals.get('Germany'))
#output: None
# currently there isn't in the list so this will return None and we will not encounter an error


#-------- some usefull methods of dictionary-------#

#print(capitals.keys()) # it will print all the keys only

#print(capitals.values()) #This will print all the values only

#print(capitals.items()) #This will print entire dictionary.

# we can also use for loop to print emtire dictionary

#for key,value in capitals.items():
    #print(key,value)

#output : 
# USA D.C
# CHINA BEIJING
# INDIA DELHI
# RUSSIA MOSCOW 
    
# one feature of dictionary is that they are mutable means we can change them or alter them after the program is already running ,
    # so one way to do that using update method of dictionaries.

# capitals.update({'Germany':'Berlin'})

# for key,value in capitals.items():
#     print(key,value)

#output: 
# USA D.C
# CHINA BEIJING
# INDIA DELHI
# RUSSIA MOSCOW
# Germany Berlin 

#So , we successfully added new key value pair 

# capital['Germany']='Berlin' #another way to add key value pair

# Using update method we can update an existing one , let say we want to change capital of INDIA

# capitals.update({'INDIA':'KARACHI'})

# for key,value in capitals.items():
#      print(key,value)

# We can also remove any key value pair for dictionary using pop method

# capitals.pop('CHINA')
# for key,value in capitals.items():
#       print(key,value)

#OUTPUT :      
# USA D.C
# INDIA DELHI
# RUSSIA MOSCOW  

# here we used pop method and using key in pop method we successfully removed china  

# del capitals['USA'] #Another way to delete any key value pair from dict.


# to clear everything
# capitals.clear()
# for key,value in capitals.items():
#     print(key,value)

# so this will clear my dictionary


 # I want to create a dictionary which will have dictionaries and list inside....so

prog={'js':'Atom','cs':'vs','python':['Pycharm','sublime'],'java':{'JSE':'Netbeans','JEE':'Eclipse'} }

  # list inside a dict and then dict inside a dict .... 2 and 3 index

#print(prog)

# output:
# {'js': 'Atom', 'cs': 'vs', 'python': ['Pycharm', 'sublime'], 'java': {'JSE': 'Netbeans', 'JEE': 'Eclipse'}}

# output looks ok , now 

#print(prog['cs']) #output : vs

#print(prog['python']) #output : ['Pycharm', 'sublime']

# we can also specify index number here which one we want ,

#print(prog['python'][1]) # output : sublime


# But what if you specify java in this case  

#print(prog['java'])

#output: {'JSE': 'Netbeans', 'JEE': 'Eclipse'}

# here we can see dictionary it self as the output but what if you want it for java EE , in this case....

#print(prog['java']['JEE']) #output : Eclipse

# ya , it is that simple ... from java we got JEE and from JEE we got Eclipse