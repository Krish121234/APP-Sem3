file = open("myfile.txt", "r+")
print(file.read())
file.write("\nAppended text")
file.close()