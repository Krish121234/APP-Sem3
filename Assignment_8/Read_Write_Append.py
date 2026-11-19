# Write
file = open("student.txt", "w")
file.write("Name: Sriraj\n")
file.write("Roll No: 23\n")
file.close()

# Append
file = open("student.txt", "a")
file.write("Course: Computer Science\n")
file.close()

# Read
file = open("student.txt", "r")
print(file.read())
file.close()
