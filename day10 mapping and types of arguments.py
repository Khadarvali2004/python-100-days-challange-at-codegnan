# 1. Function to check even or odd
"""def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

num = int(input("Enter a number: "))
result = check_even_odd(num)
print(f"The number {num} is {result}.")
print()"""

# 2. Subtraction using positional arguments
"""def sub(n1, n2):
    return n1 - n2

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("a - b =", sub(a, b))
print("b - a =", sub(b, a))
print()"""

# 3. Subtraction using keyword arguments
"""def subtract_using_keywords(a, b):
    print("Using keyword arguments:")
    print(sub(n1=a, n2=b))
    print(sub(n1=b, n2=a))
    print()"""
# 4. List properties and indexing
"""lst = [10, 2, 4, 4.534, 'hi', 'hello']
print("List elements:", lst)
print("Index 2:", lst[2])
print("Index -3:", lst[-3])
print("Slicing from index 2:", lst[2:])
print()"""
# 5. List mutability
"""lst2 = [1, 2, 3, 40, 'hi', 'hello']
lst2[0] = 100
print("Modified list (mutable):", lst2)
print()"""
# 6. Nested list access
"""nested_lst = [1, 2, 3, 4, [10, 30, 50, ['a', 'b', 'c']], 29, 1, 3]
print("Nested list:", nested_lst)
print("Inner list:", nested_lst[4])
print("Element 30:", nested_lst[4][1])
print()"""
# 7. Read list and modify values
#    Even → add 0.5
#    Odd  → add 1
def modify_numbers():
    data = input("Enter numbers separated by space: ")
    numbers = list(map(int, data.split()))

    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            numbers[i] = numbers[i] + 0.5
        else:
            numbers[i] = numbers[i] + 1

    return numbers
result = modify_numbers()
print("Updated list:", result)






