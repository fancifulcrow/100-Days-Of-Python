# Inheritance

class Animal:
    def __init__(self):
        self.no_of_eyes = 2

    def breathe(self):
        print("Inhale, Exhale")

# syntax for inheritance
# class Child(Parent):
#     def __init__(self):
#         super().__init__(self)

# Note that calling super() is recommended although not necessary
# In the child class you can override attributes and behaviours


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def swim(self):
        # super().breathe() would call the breathe function of the parent class/superclass Animal
        super().breathe()
        print("Moving in the water")


fish = Fish()
fish.swim()
fish.breathe()
print(fish.no_of_eyes)

# list and tuples can be sliced in python
a_list = ["a", "b", "c", "d", "e", "f", "g"]

# output is c, d, e
print(a_list[2:5])

# output is c, d, e, f, g
print(a_list[2:])

# output is a, b, c, d, e
print(a_list[:5])

# output is c, e
# the last number is the step
print(a_list[2:6:2])

# output is a, c ,e, g
print(a_list[::2])

# output is g, f, e, d, c, b, a
print(a_list[::-1])

# This also works for tuples
piano_notes = ("do", "re", "mi", "fa", "so", "la", "ti")
print(piano_notes[2:5])
