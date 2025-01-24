# find odd number
from operator import truediv

# numbers = int(input("Enter your number :"))
# if numbers % 2 ==0:
#     print("Even Number")
# else:
#     print("Odd Number")


    # find odd number but loop
while True:
    numbers = int(input("Enter your number or number 0 exit : "))
    if numbers == 0:
        print("it's exit program...")
        exit()
    if numbers % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

