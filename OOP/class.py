class Persons:
    # statement
    name = ""
    age = None
    job = None
# is the class persons
chhunyeang = Persons()
leangHorn = Persons()
apsor = Persons()
name = chhunyeang.name = "chhunyeang"
age = chhunyeang.age = 25
job = chhunyeang.job = "Instructor"

leangHornName = leangHorn.name = "leangHorn"
leangHornAge = leangHorn.age = 25
leangHornJob = leangHorn.job = "Student"

# information's apsor
apName= apsor.name="Apsor"
apAge=apsor.age="17"
apJob=apsor.job="Student"
print(f"Your name :{name}Your age :{age},Your Job :{job}")
print(f"Your name :{leangHornName}Your age :{leangHornAge},Your Job :{leangHornJob}")
print(f"Your name :{apName}Your age :{apAge},Your Job :{apJob}")

