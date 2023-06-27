#---------- Common Errors ----------#
# FileNotFound
# with open("missing_file.txt", "r") as file:
#     file.read()

# KeyError
# test_dictionary = {"key": "value"}
# value = test_dictionary["non_existent_key"]

#IndexError
# fruits_list = ["Apple", "Orange", "Banana"]
# fruit = fruits_list[5]

#TypeError
# text = "abc"
# print(text + 5)


#---------- Keywords for Catching Exception in Python ----------#
"""
- try: Something that might cause an exception
- except: Do this if there was an exception
- else: Do this if there were no exception
- finally: DO this no matter what happens

- raise: to raise our own exceptions
"""


#---------- Catching Exceptions ----------#
try:
    file = open("missing_file.txt", "r")
    
    test_dictionary = {"key": "value"}
    print(test_dictionary["non_existent_key"]) # A different kind of error from the above

except FileNotFoundError:
    print("We are handling the FileNotFound error")
    file = open("missing_file.txt", "w")
    file.write("Something")

except KeyError as err:
    print("That key does not exist")

else:
    content = file.read()
    print(content)

finally:
    file.close()
    print("File was closed")

    # would cause a TypeError to be raised regardless of if it actually exists
    # raise TypeError("This is an error that we made up")

# Avoid using a broad exception clause i.e. Do not use bare "except"
# We can also have multiple expection clauses


# BMI calculator
height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)


#---------- Handling JSON ----------#
# Remember to import the json package in python
# Write: json.dump()
# Read: json.load()
# Update: json.update()
