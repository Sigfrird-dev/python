# r = read
# a = append
# w = write
# x = create
import os
# *************Read - error if its doesn't exist***********

# file = open("file1.txt")
# print(file.read())
# print(file.read(4))

# print(file.readline())
# print(file.readline())

# for line in file:
#     print(line)

# file.close()

# try:
#     file = open("file3.txt")
#     print(file.read())

# except:
#     print("The file you want to read doesn't exist")

# finally:
#     file.close()


# **************append - creates the file if it doesn't exist**************

# file = open("file2.txt", "a")
# file.write("Neil\n")
# file.close()

# file = open("file2.txt")
# print(file.read())
# file.close()

# **************Write (overwrite)*****************

file = open("context.txt", "w")
file.write("I deleted all of the context")
file.close()

file = open("context.txt")
print(file.read())
file.close()


# ************** Two ways to create a new file************
# Opens a file for writing, creates the file if it doesn't exist

file = open("name_list.txt", "w")
file.close()

# Create the specified file, but returns an error if the file exists
if not os.path.exists("Dave.txt"):
    file = open("Dave.txt", "x")
    file.close()

# Delete a file
# avoid an error if it doesn't existe

if os.path.exists("Dave.txt"):
    os.remove("Dave.txt")

else:
    print("the file you wish to delete does not exist")

if os.path.exists("name_list.txt"):
    os.remove("name_list.txt")

else:
    print("the file you wish to delete does not exist")

with open("file2.txt") as file:
    content = file.read()

with open("file1.txt", "w") as file:
    file.write(content)
