#Given a positive integer x, the task is to print the numbers from 1 to x in the order
#  as 12, 22, 32, 42, 52, ... (in increasing order).
a = int(input("Enter the input about which the square value should be less than  : "))
for i in range (1,a+1):
    sq = i**2
    # print(i)
    if a >= sq:
        print(sq)