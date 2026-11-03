
import os
import shutil


# 1. Create Folder proj/logs
logs_path = os.path.join("proj", "logs")

os.makedirs(logs_path, exist_ok=True)
os.makedirs(logs_path, exist_ok=True)


# 2. Create Three Files Inside logs
a_path = os.path.join(logs_path, "a.txt")
b_path = os.path.join(logs_path, "b.txt")
c_path = os.path.join(logs_path, "c.csv")

with open(a_path, "w") as file:
    file.write("alpha\nbeta\n")

with open(b_path, "w") as file:
    file.write("gamma\n")

with open(c_path, "w") as file:
    file.write("x,y\n1,2\n")


# 3. Print Sorted List of .txt Files
txt_files = sorted(
    file for file in os.listdir(logs_path)
    if file.endswith(".txt")
)

print(txt_files)


# 4. Read a.txt and Print Number of Lines and First Line
with open(a_path, "r") as file:
    lines = file.readlines()

print(len(lines), lines[0].strip())


# 5. Move a.txt into archive Folder
archive_path = os.path.join("proj", "archive")

os.makedirs(archive_path, exist_ok=True)

new_a_path = os.path.join(archive_path, "a.txt")

shutil.move(a_path, new_a_path)

print(sorted(os.listdir(logs_path)), sorted(os.listdir(archive_path)))


# 6. Rename b.txt to old_b.txt
old_b_path = os.path.join(logs_path, "old_b.txt")

os.rename(b_path, old_b_path)

print(
    os.path.exists(b_path),
    os.path.isfile(old_b_path)
)


# 7. Delete Complete proj Folder
shutil.rmtree("proj")

print(os.path.exists("proj"))


# Main Program: B_main_module.py

# Method 1: Import whole module
import datetools

print(datetools.is_leap_year(1900))


# Method 2: Import specific names
from datetools import is_leap_year, DATE_FORMAT

print(is_leap_year(2000), DATE_FORMAT)


# Method 3: Import module using alias
import datetools as dt1

print(dt1.day_name("2026-03-08"))


# 4. Print Public Names
public_names = sorted(
    name for name in dir(datetools)
    if not name.startswith("_")
)

print(public_names)


# 5. Print Module Name and Main File Name
print(datetools.__name__)
print(__name__)

# The guard runs only when datetools.py is executed directly, not when imported.


