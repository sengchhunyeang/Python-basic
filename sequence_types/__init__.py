# Testing sequence type
from operator import truediv

my_list=[1,1.2,"String",True,45]
print("This is myList",my_list)
print("index 0 =",my_list[0])
print("index 1 =",my_list[1])
print("index 2 =",my_list[2])
print("index 3 =",my_list[3])

# print last list element
print("="*40)
print("last element".center(30))
print("="*40)

print("last element =",my_list[-1])
print("\033[92m" + "="*40 + "\033[0m")
# Reassign
print("Reassign element in list".center(30))
print("\033[92m" + "="*40 + "\033[0m")


# color border https://gist.github.com/rene-d/9e584a7dd2935d0f461904b9f2950007

# Modifying elements
my_list[2] = "Apple"
my_list[-1] = "10"
print("This is myList",my_list)

# adding Element
my_list.append("Banana")
print("This is myList added =",my_list)