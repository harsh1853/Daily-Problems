#To pring the right angle triangel of numbers
a = int(input("Enter the upto number : "))
i = 1 
j = 1
for i in range (1,a+1):
    for j in range (1,i+1):
        print(j,end=" ")
        j = j+1
    print("\n")
    i = i+1

        
    