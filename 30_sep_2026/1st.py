#Given a number n, print the multiplication table 
# from 1 to 10 for n in a single line, separated by spaces.
n = int(input("Enter the number you want table of : "))
for i in range (1,11):
    i = i*n
    print(i,end=" ")