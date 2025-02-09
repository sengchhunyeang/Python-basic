numbers = [1, 2, 2, 35, 58, 69, 52]

# Find even numbers
# even_numbers = [num for num in numbers if num % 2 == 0]
# print("Even numbers:", even_numbers)
#
# for num in numbers:
#     if num % 2 != 0:
#         print(num)

list1 = [num for num in numbers if num % 2 == 0]
print("Even number :",list1)
list2 = [num for num in numbers if num % 2 != 0]
print("odd number :",list2)
