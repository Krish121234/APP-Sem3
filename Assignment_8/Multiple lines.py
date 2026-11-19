lines = ["First line\n", "Second line\n", "Third line\n"]
file = open("myfile.txt", "w")
file.writelines(lines)
file.close()