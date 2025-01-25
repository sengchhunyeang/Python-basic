# String Handling
# 1 Create String
my_string = "Hello World"
my_string2 = 'This is also a string.'

# Access Character
# 2 Accessing Characters
# Print Only fist and last
first_char = my_string[0]
last_char = my_string[-1]
print("=" * 50)
print("first char:", {my_string}, first_char)
print("last char :", {my_string}, last_char)

# 3. Slicing
# Syntax: string[start:end]

print("\033[0;36m=" * 50)
print(my_string[6:12])

# 4. String Concatenation
concatenation = my_string + my_string2
print(concatenation)

my_string = "Hello, World!"

# 1. Uppercase
print(my_string.upper())  # Output: "HELLO, WORLD!"

# 2. Lowercase
print(my_string.lower())  # Output: "hello, world!"

# 3. Find substring
print(my_string.find("World"))  # Output: 7 (index of the first occurrence of "World")

# 4. Replace substring
print(my_string.replace("World", "Universe"))  # Output: "Hello, Universe!"

# 5. Split the string
words = my_string.split(",")
print(words)  # Output: ['Hello', ' World!']

# 6. Join a list of strings
words = ["This", "is", "a", "sentence"]
sentence = " ".join(words)
print(sentence)  # Output: "This is a sentence"