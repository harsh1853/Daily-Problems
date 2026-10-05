# 1. In python list is a collection which is used to store data 
# 2. Lists are muttable and can be edited as well as updates 
# 3. Function are the important list terms which do not edit or change the already existing data 
#    but thye just print , show or arrange the already existing data of the list 
# 4. Syntax of a funtion --> fun_name(list_name)

# Some importrant list functions 
l = [4,35,3,87,90,3,43,90,34,1,2,43,0]

1. # len(list_name) --> To print the length of the list 
print(len(l))

2. # max(list_name) --> Returns the max element of the list 
print(max(l))

3. # min(list_name) --> Returns the min element of the list 
print(min(l))

4. # sum(list_name) --> Return the sum of all element in the list
print(sum(l))

5. # sorted(list_name) --> Returns the list in an ascending order
print(sorted(l))

6. # reversed(list_name) --> Return the list in descending order 
                             #but it return at a memory address to get that address we convert into a list
print(list(reversed(l))) 
print(sorted(l,reverse=True))

7. # any(list_name) --> Returns True if at leat one element is true means non-zero
                # if all elements are zero it returns false
print(any(l))

8. # all(list_name) --> Returns true if every element is non-zero
                  # if even 1 element is zero it will return false
print(all(l))