class Person:
    def __init__(self):
         self.name=None
         self.age=None
         self.height=None
    
    def __str__(self):
         return f"Person(name: {self.name}, age: {self.age}, height: {self.height})"
 
    def working(seft,nameWork):
        print(f"working on :{nameWork}")
        
        
person = Person()

person.name="chhunyeang"
person.age=34
person.height=175
person.working("Developer")
print(person)
