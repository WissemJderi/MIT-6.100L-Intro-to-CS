counter = 0
largest = 0
while counter < 10:
    integer = int(input("Enter An int: "))
    
    
    if integer % 2 != 0 :
        if largest < integer:
            largest = integer
    else:
        print("this is not an integer")
        
    counter += 1
    
print(largest)
    
