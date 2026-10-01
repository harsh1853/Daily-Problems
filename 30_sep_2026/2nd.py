#Given a number x, the task is to print the numbers
#  from x to 0 in decreasing order in a single line.
a = int(input("Enter the number : "))
i = a
while i >= 0:
    print(i,end = " ")
    i = i-1
