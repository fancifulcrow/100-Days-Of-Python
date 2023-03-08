import random

# generating random integers
random_int = random.randint(1, 10)
print(random_int)

# generating random floats
# randomizing floats between 0.0 and 5.0
random_float = random.random() * 5
print(random_float)
# note that the random generation would only go up to 4.999999999


# Lists
fruits = ["Cherry", "Pineapple","Banana", "Apple", "Orange"]
vegetables = ["Spinach", "Carrot", "Cabbage", "Lettuce", "Celery"]

print(fruits[0])
print(fruits[-1])
# Check doc.python.org for the documentation
fruits.append("Strawberry")
fruits.extend(["Watermelon", "Blueberry", "Guava"])
print(fruits)

# IndexError
# be careful with the size of arrays

# Nested List
food = [fruits, vegetables]