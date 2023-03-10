import random

# List Comprehension
#new_list = [new_item for item in list]

numbers = [1, 2, 3, 4, 5]
new_list = [n + 1 for n in numbers]
print(new_list)

name = "Angela"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [n * 2 for n in range(1, 5)]
print(range_list)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]
print(short_names)
long_names = [name.upper() for name in names if len(name) > 5]
print(long_names)

# Dictionary Comprehension
# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key, value) in dict.items()}

student_scores = {student:random.randint(1, 100) for student in names}
passed_student = {student:score for (student, score) in student_scores.items() if score >= 60}
print(student_scores)
print(passed_student)

# Iterate over Pandas DataFrame
import pandas

student_dict = {
    "student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 90],
}
student_dataframe = pandas.DataFrame(student_dict)
print(student_dataframe)
for (index, row) in student_dataframe.iterrows():
    if row.student == "Angela":
        print(row)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}