# review
# what is a class ?
# => class is a blueprint for create a object

# What is an object in Python?
#
# How to define a class

class Student:  # class stundent
    # stetement
    def __init__(self, student_id, student_name, student_age, student_gender):
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age
        self.student_gender = student_gender

    def printer(self):  # for show information student
        print(
            f"Student Information \n StudentId : {self.student_id} \n StudentName : {self.student_name}  \n StudentAge : {self.student_age} \n StudentMale :{self.student_gender}"
        )


# objectName = ClassName()
id = input("ID: ")
name = input("student name : ")
age = input("student age : ")
gender = input("student gender: ")
objectName = Student(id, name, age, gender) # user set value

objectName.printer()

    