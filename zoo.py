#Create a tuple named zoo that contains your favorite animals.
zoo = ("peacock", "giraffe", "elephant")
print("The animals in my zoo: ", zoo)

# Find one of your animals using the .index(value) method on the tuple.
zoo_index = zoo.index("giraffe")
print("The index of giraffe is: ", zoo_index)

# Determine if an animal is in your tuple by using for value in tuple.
print("Is the giraffe in the zoo?  Answer:","giraffe" in zoo)

# Create a variable for each of the animals in your tuple with this cool feature of Python.
    # example
    # (lizard, fox, mammoth) = zoo
    # print(lizard)

(peacock, giraffe, elephant) = zoo
print("The variable peacock has been assigned to the string value:", peacock)
print("The variable 'peacock' is a:", type(peacock))

# Convert your tuple into a list.
tuple_to_list = list(zoo)
print(type(tuple_to_list))

# Use extend() to add three more animals to your zoo.
tuple_to_list.extend(("Lion", "Kangaroo", "Penguin"))
print(tuple_to_list)
# Convert the list back into a tuple.
list_to_tuple = tuple(tuple_to_list)
print(type(list_to_tuple))
print(list_to_tuple)