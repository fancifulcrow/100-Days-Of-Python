# You are going to write a program that calculates the average student height from a List of heights.
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

# Write your code below this row 👇
sumOfStudentHeight = 0
noOfStudents = 0

for height in student_heights:
    sumOfStudentHeight += height

for num in student_heights:
    noOfStudents += 1

averageOfStudentHeight = round(sumOfStudentHeight/noOfStudents)
print(averageOfStudentHeight)

# using sum() and len()
# sumOfStudentHeight = sum(student_heights)
# noOfStudents = len(student_heights)
# averageOfStudentHeight = round(sumOfStudentHeight/noOfStudents)