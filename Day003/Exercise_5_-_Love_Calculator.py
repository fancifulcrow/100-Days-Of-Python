# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combinedString = name1 + name2
lowercase_name = combinedString.lower()

t = lowercase_name.count("t")
r = lowercase_name.count("r")
u = lowercase_name.count("u")
e = lowercase_name.count("e")

true = t + r + u + e

l = lowercase_name.count("l")
o = lowercase_name.count("o")
v = lowercase_name.count("v")
e = lowercase_name.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score > 40 and love_score < 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your score is {love_score}.")