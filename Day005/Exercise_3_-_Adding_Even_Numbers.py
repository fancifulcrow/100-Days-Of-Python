# You are going to write a program that calculates the sum of all the even numbers from 1 to 100
#Write your code below this row 👇
sumOfEvenNumbers = 0

for number in range(1, 101):
    if number % 2 == 0:
        sumOfEvenNumbers += number

# This also works
# for number in range(2, 101, 2):
#     sumOfEvenNumbers += number

print(sumOfEvenNumbers)