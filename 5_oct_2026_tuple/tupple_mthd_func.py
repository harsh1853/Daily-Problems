# Tuple : Tuples are immutable and they do not support item assignment 
# --> We cannot add a value in a tuple but we can do (add old tuple) + (new values tuple)

# --> it is impossible to edit , change or modify teh already existing data in tuples 
# --> syntax --> tup = () , empty tuple --> tup = (,)

t = (10,23,45,290,3,2,4,5,3,2,90,10,290)

# Tuple Methods : There are only two tuple methods 

1. # tup.count(data) --> Used to cound the number of times an element in tuple
print(t.count(10))

2. # tup.index(data) --> Return the 1st index at which that value showed up 
print(t.index(10))

# Tuple Functions :

1. # len(tup)
print(len(t))

2. # max(tup)
print(max(t))

3. # min(tup)
print(min(t))

4. # sum(tup)
print(sum(t))

5 # sorted(tup) --> The output of the sorted will be stored in  list as tuple
                # does not supports item assignment and for sorting item assignment is necessary
print(sorted(t)) 

6. # reversed(tup) --> The outpot will be stored at a memory address so typecast to store in a list or tuple
print(list(reversed(t))) 

7. # tuple([datas]) --> converts the data into tuple
print(tuple([3,2,53,56])) # --> This list [3,2,53,56] becomes a tuple 

8. # all(tup) --> Returns true only if all the values are non zero
print(all(t))

9. # any(tup) --> Returns true only if atlest one value is non-zer
print(all(t))
