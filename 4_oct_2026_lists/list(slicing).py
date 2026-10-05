# String Slicing 
# syntax --> list_name[start:stop:step] stop is always executed 

1. # Complete slicing 
l = [10,20,30,50]
print(l[0:]) 
print(l[::])
print(l[0:len(l):1])

2. # Negative slicing 
print(l[-1])  # --> This will print the last elemet of the list
print(l[::-1]) #--> This will reverse the list 
print(l[-1::-1])