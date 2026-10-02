n = int(input("Enter the number: "))

multiple = []

# Create tables
for i in range(1, n + 1):
    table = []

    for j in range(1, 21):
        table.append(i * j)

    multiple.append(table)

print(multiple)

# Find common multiples
common = []

for k in multiple[0]:
    found = True

    for table in multiple:
        if k not in table:
            found = False
            break

    if found:
        common.append(k)

print("Common multiples:", common)
print("Lowest common multiple:", common[0])
    

            
    

    
    
    