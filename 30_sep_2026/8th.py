#You are given an integer n. You need to convert all zeroes of n to 5.
a = str(input("Enter the number : "))
lis =[]
new_lis = []
# d = int(i)
for i in a:
    # print(i)
    lis.append(i)
d = int(i)
# print(type(i))
# print(lis)
for j in lis:
    if j == '0':
        j = '5'
        new_lis.append(j)
    else:
        new_lis.append(j)
# print(new_lis)
for k in new_lis:
    print(k,end="")




        
    
   
