# what is list ?
# list are use stored multiple item in single variable
# How to Declare list

# myCar=["Toyota","Ford","Camary"]
# print(myCar)
# print(myCar[2])

student_marks=[]
for i in range(5):
    mark = float(input("Enter the marks: "))
    student_marks.append(mark)
average_mark=sum(student_marks)/len(student_marks)
if average_mark >=50:
    print("your average mark is:",average_mark)
    print("Pass")
else:
    print("your average mark is:",average_mark)
    print("Fail")