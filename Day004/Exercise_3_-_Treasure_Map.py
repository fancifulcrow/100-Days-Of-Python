# You are going to write a program that will mark a spot with an X.
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# if the position was at column 2 and row 3 write "23"
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

horizontal = int(position[0]) - 1
vertical = int(position[1]) - 1

selected_row = map[vertical][horizontal] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")