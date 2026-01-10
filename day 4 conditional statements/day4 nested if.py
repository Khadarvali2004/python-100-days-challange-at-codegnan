num = int(input("Enter a number: "))
if num > 0:
    print("The number is positive.")
    
    if num % 2 == 0:
        print("It is an even number.")
    else:
        print("It is an odd number.")
else:
    print("The number is zero or negative.")
