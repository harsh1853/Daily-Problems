# The operations that we can perform on multiple dict

d1 = {
    "Name" : "Harsh",
    "Roll no" : 6339,
    "College" : "NBNSTIC"
}

d2 = {
    "Address" : "Pune",
    "Ph no" : 8924834830,
    "Age" : 21
}

1. # Merging two dictionary 
d3 = d1 | d2 # this is going to work as d3 = d1+d2
print(d3)

2. # Merging one dictionary into the other one
d1 = d1 | d2 # dictionary d2 is getting added in d1 itself 
print(d1) 

3. # dict_name[key]  --> To get the value of a key 
print(d1["Name"])

