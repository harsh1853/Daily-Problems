#Dictionalry --> These are the collection in python which store the dats in form of keys and values 
# syntax --> dict_name = {
                            # "key1" : "value" ,
                            # "Key2" : "Value" ,
                            # }

d = {
    "Name" : "Harsh" ,
    "Class" : "TE-2" ,
    "Roll no" : 5534 ,
    "College" : "NBNSTIC"
}

# Dict functions 

#1.len(d) --> Prints the number of the key value pairs 
print(len(d))

#2.str(d) --> Converts the dict to a string 
# print(str(d))

#3. sorted(d) --> Sort the keys accoring to the ASCII values (only keys)
print(sorted(d))

#4. min() and max() --> They print the smallest keys (only keys)
print(min(d) , max(d))

#5. sum() --> Prints the sum of values (only values)
#sum(d.values()) #--> It wil show error as value has both string as wel as int so addition is not possible 
# sum(d.key())

#6. any() --> Returns true if any value is non-zer (scans only values)
print(any(d.values()))

#7. all() --> Returns true if all the values are non-zero 
print(all(d.values()))


# Dict Methods 

#1. clear()
# d.clear()
print(d)

#2. copy()
d1 = d.copy()
print(d1)

#3.fromkeys() --> creats a new dictionary , means in the already existing list the elements are treated like keys
                 # while the values is assigned by us and we can assign same values to every elemet (every key)
#Syntax --> d1 = dict.fromkeys(list,"Value")

l = ["Name","Age","Date"] # --> This is the list whose elements will be treated like keys

d1 = dict.fromkeys(l,"Unknown") #--> Unknown will be the values which will be assigned to all the keys or the elements of the list
print(d1)

#4. get() --> Used to get the value from the key without causing error in case that  key is not present 
print(d.get("Name"))
# If the given key does not exist it will simply return none 

#We can also provide a default 
print(d.get("Marks" , 87)) #--> This wont be included in teh original dict
print(d)

#5. items() --> Return all the key values pairs in a list
print(d.items())

#6. keys() and values() --> They return all the keys and values of the dict in a list 
print(d.keys()) 
print(d.values())

#7. pop() --> Removes the specifed keya nd returns its value 
d.pop("College")
print(d) # --> The key and value pair of college got removed 

#8.popitem() --> Removes the last inserted key-value pair
d.popitem()
print(d)

#9.update() --> Add or modifies multiple key value pairs
d.update({"Name" : "Aditya" , "Age" : 21})
print(d) #--> Already existing value Harsh got updated and new key value pair age 21 is added in dict

#10. del d[key] --> It wil delete the key 
del d["Age"]
print(d)
