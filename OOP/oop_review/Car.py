class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def show_info(self):
        print(f" Car Info:\nBrand: {self.brand}\nModel: {self.model}\nYear: {self.year}\nColor: {self.color}")

#  User input to create a Car object
brand = input("Enter car brand: ")
model = input("Enter car model: ")
year = input("Enter car year: ")
color = input("Enter car color: ")

# Creating an object (instance) of the Car class
my_car = Car(brand, model, year, color)

# Display car information
my_car.show_info()


student_id = input("")


