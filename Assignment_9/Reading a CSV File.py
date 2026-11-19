import csv

filename = "student_records.csv"

# Reading CSV File
with open(filename, mode="r", encoding="utf-8") as csvfile:
    csvreader = csv.reader(csvfile)

    # Extract field names (header)
    fields = next(csvreader)
    print("Field Names:", ", ".join(fields))

    # Extract rows
    rows = []
    for row in csvreader:
        rows.append(row)

    print(f"Total number of rows: {csvreader.line_num - 1}\n")

    # Displaying first 5 rows
    print("First 5 rows:")
    for row in rows[:5]:
        print(row)