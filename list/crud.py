# create list
my_list=["A","B","C"]
print(my_list)
#insert
my_list.append("E")
print("inserted :", my_list)
#update list
my_list[0]="D"
print("My list updated :",my_list)

# remove list
my_list.remove(my_list[3])
print("my list removed :",my_list)

def greeting(name):
    print("Hello:",name)