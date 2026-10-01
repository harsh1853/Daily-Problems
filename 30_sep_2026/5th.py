#to print the largest of the 3 numbers 
n1 = int(input("Enter the 1st number : "))
n2= int(input("Enter the 2nd number : "))
n3 = int(input("Enter the 3rd number : "))
if n1 >= n2 and n1 >= n3:
    print(n1)
elif n2 >= n3:
    print(n2)
else:
    print(n3)