# Loop ....

# # while loop and for
#
# i = 4 # value start 1
# n = 1 # value end 5
# while i >= n: # check condition
#     print(i)
#     i -=1 # i =i-1
#
# # 4 -1
# # 3 - 1
# # 2 - 1
# # 1 - 1

# total =0 #2  + 2 +2 = 6
# number = int(input("number input : "))
# while number != 0: # condition input value !=0 1-9
#     total += number
#      = int(input("number input : "))
# print("total :",total)


# find number odd number and even number
# loop ......... it stop false

# Pratice
# 1,2,3,....10
# 10,9,8,.....1
# using while loop


print('System Information:', 'Shortcuts', '0 - exit program', '1 - Subject Average calculator',
      '2 - Multiplication Calculator')
s = int(input('which feature would you like to use? ')) # this find your issues
if s == 1:
    python = int(input('insert python grade in percentage '))
    kotlin = int(input('insert kotlin grade in percentage '))
    php = int(input('insert PHP grade in percentage '))
    java = int(input('insert Java grade in percentage '))
    R = int(input('insert R grade in percentage '))
    total = python + kotlin + php + java + R
    average = total / 5
    name = input('what is your student name? ')
    print(name, 'has acheived an average grade of', average)
