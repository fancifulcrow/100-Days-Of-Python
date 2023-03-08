# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades
# student_grades should contain student names for keys and their grades for values.

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99,
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    elif score <= 70:
        student_grades[student] = "Fail"

# 🚨 Don't change the code below 👇
print(student_grades)