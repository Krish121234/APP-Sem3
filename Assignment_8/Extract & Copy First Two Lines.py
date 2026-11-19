# Read lines and extract first two
with open("input.txt", "r") as infile:
    lines = infile.readlines()
    print("Total number of lines:", len(lines))
    first_two = lines[:2]
    print("First two lines:", first_two)

# Write extracted lines to a target file
with open("output.txt", "w") as outfile:
    outfile.writelines(first_two)
    print("Data written successfully!")