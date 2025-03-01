# numbers = [1, 2, 3, 4, 5, 6, 7]
# if numbers[0] == 1:
#     print(numbers[0])
# else:
#     print("number not ")

# what is list
# list collection that use for store value and varaible call by index
# my_list = ["Monday","Tuesday","wednesday"]
# # index = 0 ,1,2
# print(my_list)

# print("call 3td day :",my_list[2])


books = [
    "To Kill a Mockingbird",
    "1984",
    "Pride and Prejudice",
    "The Great Gatsby",
    "Moby-Dick",
    "War and Peace",
    "The Catcher in the Rye",
    "The Hobbit",
    "Harry Potter and the Sorcerer's Stone",
    "The Lord of the Rings",
    "The Da Vinci Code",
    "The Hunger Games",
    "The Alchemist",
    "The Road",
    "A Brief History of Time",
    "The Silent Patient",
    "Sapiens: A Brief History of Humankind",
    "The Girl on the Train",
    "The Book Thief",
    "The Chronicles of Narnia",
]
removed= books[1]
books.remove(removed)
print("removed variable:",removed)
print("items removed",books)
