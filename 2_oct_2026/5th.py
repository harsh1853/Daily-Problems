#see of a given term in in AP or not
a = int(input("Enter teh 1st term : "))
d = int(input("Enter teh common difference : "))
nth_term = int(input("Enter the nth term : "))
for i in range (a,(nth_term+1),d):
    if i == nth_term:
        print("Exists")
        break
    
