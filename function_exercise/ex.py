# examle 1
def printer():
    print(" welcome to python ")
    
# printer()

# example 2 

#Parameters but Has a Return Value
def number_return():
    return 5

# example 3 
def word():
    return "python"

# Example 
#Has Parameters but No Return Value
def hello(name):
    print("Hello",name)

hello("Chantha")
# Exercise 6
def number_double(number):
    return float(number) # value of double 0.0

valueA=number_double(5)
print(valueA)

# Exercise 7 

def sum(a,b):
    return a+b

valueAB = sum(5,8)

print(valueAB)


# Repeat a word 

# Hi hi hi hi

def repeat_word(word,time):
    
    return word * time

store_word= repeat_word("A",5)
print(store_word)


# Exercise 9: Check Even or Odd
# Write a function that takes a number and returns "Even" if it's even and "Odd" if it's odd.

#លេខសេស odd
#លេខគូរ Even

def check_number(number):
    
    if number % 2 == 0:
        print(number,"is Even number")
    else:
        print(number,"is odd number")
        
        
check_number(2)


# name="Chantha"

# print("Are you ",name,"?")
# print(f"Are you {name}?")
# print(f"*are you {name} ?")
# print("Are you "+name+"?")

# Exercise 10: Find the Maximum of Three Numbers
# Write function that find Max and Min of Three number.


# has param has return 
#param (a,b,c) 3 value

# return min() , max()

# 7,8,9
# max =9
# min = 7
# Exercise 10: Find the Maximum of Three Numbers
# Write function that find Max and Min of Three number.

def find_value(valueA,valueB,valueC):
    
    return min(valueA,valueB,valueC) 

def find_value_max(valueA,valueB,valueC):
    
    return max(valueA,valueB,valueC)

# print(f"Is the min number :{find_value(7,8,9)}")
# print(f"Is the max number :{find_value_max(7,8,9)}")


# funtion buil in 

# number = max(1,2,3)
# print(number)

# def loop(number):
#     for x in range()
   
 #body

# result 


# 1,2,3,4

print("="*40)
# a=1
# for x in range(a,5):
#     print(x)


def loop_number(a):
    for x in range(a,10): #rang(start,end) 
        print(x)
# loop_number(1) 

