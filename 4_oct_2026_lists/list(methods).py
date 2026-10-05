# List Methods :- These are the methods which actually perform some operation on data means the list and then return something
# syntax --> list_name.method(data)

l = [94,4,24,6,3,90,65,24,56,89,3,4]

1. # list_name.append() --> Add one item at the end of the list
l.append(2345)
print(l) #--> 2345 added at the last of the list l

2. # list_name.extend([Items]) --> to add multiple items
l.extend([76,89,34])
print(l)

3. # list_name.insert(index,element) --> inserts the given element at specified list
l.insert(3,56)
print(l) # --> Elemet 56 added at index 3 of the list l

4. # list_name.remove(elemet) --> it will remove the element which occurs at the 1st time in list
l.remove(4)
print(l) # --> Remove teh 1st time where 4 occured in the list

5. # list_name.pop() --> Removes teh last elemet of the list
l.pop()
print(l)

6. # list_name.clear() --> Removes all the element of the list
# l.clear()
# print(l)

7. # list_name.index(elemet) --> it will find the position or index of the elemet in the list
print(l.index(76))

8. # list_name.count(elemet) --> Counts the number of times an elemet showed up in the list
print(l.count(4))

9. # list_name.sort() and list_name.reverse() --> Prints the list in ascending and descending order 
l.sort()
print(l)
l.reverse()
print(l)

10. # new_list = list_name_to_be_copied.copy() --> copies the list l and stores it in l1
l1 = l.copy()
print(l1) 