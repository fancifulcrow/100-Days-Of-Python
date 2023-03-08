# Creating a class
# PascalCase is the naming convention used to name classes
# snake_case is mostly used for everything else
# camelCase is not used as much in python
class Things:
    
    pass


def function():
    # Pass keyword makes it that a function or class can be empty
    pass


thing_1 = Things()
# we can create attributes for the object
# even though the property "id" was not made in class User, it exists ONLY for user_1
thing_1.id = "001"


class Car:

    # This is a contructor
    def __init__(self, seats, color):
        self.seats = seats
        self.color = color
        # this is an attribute that all car objects would have but it does not need to be provided when constructing new objects
        self.fuel_level = 0


car_1 = Car(4, "red")
car_2 = Car(2, "blue")


class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # methods always use the "self" keyword as the first parameter
    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "angela")
user_2 = User("002", "jack")

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)