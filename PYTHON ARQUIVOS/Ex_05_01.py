largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    
    if num == "done":
        break
    
    try :
        inum = int(num)
        #print(inum)
        if largest is None or inum > largest:
            largest = inum
        
        if smallest is None or inum < smallest:
            smallest = inum
        
    except :
        print ("Invalid input")
        continue

print("Maximum is", largest)
print("Minimum is", smallest)