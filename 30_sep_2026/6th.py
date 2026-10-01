#find if leap year or not 
a = int(input("Enter the year : "))
if (a%4 == 0 and a%100 != 0 ) or (a%400 == 0):
    print("It is a leap year")
else:
    print("Not a leap year")

a = int(input("Enter the year: "))

# if a % 400 == 0 or (a % 4 == 0 and a % 100 != 0):
#     print("It is a leap year")
# else:
#     print("Not a leap year")