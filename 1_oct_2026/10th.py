#print the 2nd biggest number
n1 = int(input("Enter the 1st number : "))
n2 = int(input("Enter the 2nd number : "))
n3 = int(input("Enter the 3rd number : "))
if (n1 >= n2 and n3 >= n1 ) or (n1 >= n3 and n2 >= n3):
    print(n1)
elif (n2 >= n1 and n3 >= n2) or (n2 >= n3 and n1 >= n2):
    print(n2)
else:
    print(n3)
