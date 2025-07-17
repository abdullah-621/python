import os

# Specify the directory path (you can change this to any directory you want)
directory_path = "/Desktop/HTML & CSS/Project/Hancok"

# Get the list of files and directories
try:
    contents = os.listdir(directory_path)
    print(f"Contents of directory '{directory_path}':")
    for item in contents:
        print(item)
except FileNotFoundError:
    print("The specified directory does not exist.")
except PermissionError:
    print("You do not have permission to access this directory.")
