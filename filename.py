# import OS module
import os

# Get the list of all files and directories

dir_list = os.listdir("./")

print("Files and directories in '", "' :")

# prints all files
for name in dir_list:
    print(name)
