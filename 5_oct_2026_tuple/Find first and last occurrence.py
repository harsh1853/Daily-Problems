n = tuple(map(int, input("Enter the number : ").split()))
print(n)
n1 = int(input("Enter the number : "))
print(f"The first occurence at index {n.index(n1)}") #this will return the 1st occurent 

#to find the last occurence reverse the tuple and map it back to original index 
last_idx = len(n) - 1 - n[::-1].index(n1)
print(f"The last index is {last_idx}")
