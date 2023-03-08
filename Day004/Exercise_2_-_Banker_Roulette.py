# You are going to write a program that will select a random name from a list of names

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
totalNames = len(names)

random_nameIndex = random.randint(0, totalNames - 1)

print(f"{names[random_nameIndex]} is going to buy the meal today!")

# using the choice function it would look like this:
# personPaying = random.choice(names)
# print(f"{personPaying} is going to buy the meal today!")