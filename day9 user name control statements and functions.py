#user validation
"""s=input() #khadarvali
validate_string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@_"
if len(s) >= 8:
    #check atleast one upper case and lower case letter
        # -first charachter is upper or lower
    if s[0].isupper() or s[0].islower():
        for i in range(1,len(s)):
            if s[i]in validate_string:
                print("valid username")
            else:
                print(f"invalide username becuase charachter {s[1]}")
    
    else:
        print("user name is not valide becuase first charachter is not upper or lower")
else:
    print("not valide becuase lenth is lesss then 8 charachters") """
#loop control statement

"""for i in range(1,6):
    if i==3:
        continue
    print(i)"""
"""for i in range(1,6):
    if i==3:
        break
    print(i)"""
#function definition
"""def sum_of_two_numbers(a,b):
    s=a+b
    return(s)
res=sum_of_two_numbers(10,40)
print(res)"""
#functions
def addition (a, b):
    return a + b

def subtraction(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero"

if __name__ == "__main__":
    print("Welcome to a small level calculator")
    n1 = int(input("Enter number 1: "))
    n2 = int(input("Enter number 2: "))
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        print("Sum of two numbers is:", addition(n1, n2))
    elif choice == 2:
        print("Subtraction of two numbers is:", subtraction(n1, n2))
    elif choice == 3:
        print("Multiplication of two numbers is:", mul(n1, n2))
    elif choice == 4:
        print("Division of two numbers is:", div(n1, n2))
    else:
        print("Enter any correct operation")
