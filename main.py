# R = Reading, W = overwrite the file and adds whatever, A= open for writing new stuff to the end of the file
my_file = open("Project2.txt", 'r')
all_lines = my_file.readlines()
for lines in all_lines:
    new_lines = lines.strip()
    new_lines = new_lines.split(":")
    print(f"Student ID:",new_lines[0], "Student Name:", new_lines[2])