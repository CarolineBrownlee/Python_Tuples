# Tuples are like lists, but are immutable. They can't be modified once defined. However, finding values in a tuple is faster than in a list.

# 1. Create a tuple named zoo that contains 10 of your favorite animals.
zoo = ("cat", "Atticus", "dog", "Briley", "fish", "Zippy", "lion", "Bubba", "kangaroo", "Sammy", "shark", "Jaws", "turtle", "Sampson", "frog", "Hoppy", "monkey", "Captain Silly")

# 2. Find one of your animals using the tuple.index(value) syntax on the tuple.
this = zoo.index("Captain Silly")
# print(this)

# 3. Determine if an animal is in your tuple by using value in tuple syntax.

# animal_to_find = "Jaws"
# if animal_to_find in zoo:
#     print("The animal was found.")

# 4. You can reverse engineer (unpack) a tuple into another tuple with the following syntax.

# children = ("Sally", "Hansel", "Gretel", "Svetlana")
# (first_child, second_child, third_child, fourth_child) = children
# print(first_child) # Output is "Sally"
# print(second_child) # Output is "Hansel"
# print(third_child) # Output is "Gretel"
# print(fourth_child) # Output is "Svetlana"

# Create a variable for the animals in your zoo tuple, and print them to the console.

