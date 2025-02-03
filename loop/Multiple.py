
number = int(input("Enter a number:"))

# Define the range of multipliers
start = 1
end = 10  # You can change this to any number you want

# Loop through the range and print the multiplication table
for i in range(start, end + 1):
    result = number * i
    print(f"{number} * {i} = {result}")