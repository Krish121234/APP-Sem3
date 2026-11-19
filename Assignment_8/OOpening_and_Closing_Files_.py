# Open in read mode and explicitly close
file = open("myfile.txt", "r")
print(file.read())
file.close()