# Read the file
with open("../../my_file.txt") as file:
    contents = file.read()
    print(contents)

# Write the file
# with open("my_file.txt", mode="w") as file:
#     contents = file.write("Hello")

# append the file
# with open("my_file.txt", mode="a") as file:
#     contents = file.write("Hello")