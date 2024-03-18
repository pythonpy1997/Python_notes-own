name="Tamal Mondal"
name1="tamal mondal"
name2="TAMAL MONDAL"
number="1234"
name_alpha="TamalMondal"

print(len(name)) #This str method use to know str length.

print(name.find("d")) #using find str method we can find character.

print(name1.capitalize()) #using this str method we can capitalize str but if space between 2 words in str then it will not work after space.

print(name1.upper()) #use to upper case entire string

print(name2.lower()) #use to lower case entire string

print(name.isdigit()) #use to check str is number or not and return output as boolean (True/False)

print(number.isdigit()) # now it will return true because in variable we store numbers as str.

print(name.isalpha()) #use to check str alphabets or not , but if space found then it will return False

print(name_alpha.isalpha()) #now it is showing True output because no space in between.

print(name.count("a")) #use to count how many perticular character there , exp. here total three "a" available.

print(name.replace("a","i")) #use to replace one character to other character , like here we did replace "a" to "i" .

print(name*3) #this is technically not method , but it's a cool feature. 

