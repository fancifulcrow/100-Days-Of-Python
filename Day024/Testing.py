# Open a file
file = open("my_file.txt")

# Read the contents of the file
content = file.read()
print(content)

# Always close the file to save resources and improve performance
file.close()

# You could write the code like this, using the "with" keyword so that you don't need file.close()
with open("my_file.txt") as f:
    notes = f.read()
    print(notes)

# Write content to a file
# mode "r" is read, mode "w" is write, mode "a" is append
with open("my_file.txt", mode="w") as txt:
    txt.write("Hello World from 'w' mode")

with open("my_file.txt", mode="a") as doc:
    doc.write("\nHello World from 'a' mode")

# If the file does not exist, python with automatically create it
with open("new_file.txt", mode="w") as page:
    page.write("This is a new document")

# File Paths
# Absolute Paths and Relative Paths
# Once we establish a Working Directory, we can the use Relative Paths
