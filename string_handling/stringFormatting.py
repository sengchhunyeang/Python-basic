# 1,Basic f-string
name="Chhunyeang"
age=24
print(f"Hello, {name}! You are {age} years old.")

# 2  Formatting numbers
print("\033[1;33m="*50+ "\033[0m")
# print("\033[92m" + "="*40 + "\033[0m")
pi = 3.14159
radius = 5
area = pi * radius**2
print(f"The area of the circle is: {area}")
print("\033[1;33m="*50+ "\033[0m")
print(f"The area of the circle is: {area:.2f}")

