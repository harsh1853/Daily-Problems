#code to compare 3 numbers
n1 = int(input("Enter 1st number"))
n2 = int(input("Enter 2nd number"))
n3 = int(input("Enter 3rd number"))
if n1 == n2 and n2 == n3:
    print("All the given numbers are equal")
if n1>=n2 and n1>=n3 :
   print(f"{n1} is the greatest")
elif n2>=n1 and n2>=n3:
    print(f"{n2} is the greatest number")
else:
    print(f"{n3} is the greatest")


    



   

