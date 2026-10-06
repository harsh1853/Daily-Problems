# Operations that can be performed on tuples: 

t1 = (1,2,3,4)
t2 = (10,20,30,40)
t3 = (100,200,300,400)

1. # Slicing --> As same as list 

2. # Concatation --> Combining two or more tuples 
print(t1+t3+t2) # --> Makes a new tuple combining t1 , t2 and t3

3. # Multiplication --> Prints the same tuple n numbe of times
print(t1*2)

4. # Checking membership --> x in t1 --> Returns true or false 
print(100 in t3) #--> prints True as 100 exists in t3

5. # Comparison of two tuples a.Equality
print(t1==t2) #--> Prints false 

6. # t1 > t2
print(t2>t1) #--> True as each and every elemet of t2 is greater than t1


# 7. enumerate --> Very important 
#--> This prints the index and element in a keyword and value pairs 
#--> Enumerate itself cannot hold any values it just prints the memory address
     # where the value is store we can typecast that into a list get the output
     
print(list(enumerate(t1))) 
