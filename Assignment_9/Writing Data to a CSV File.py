import csv

# Header and data rows
fields = ["Name", "Branch", "Year", "CGPA"]
rows = [
    ["Nikhil", "COE", "2", "9.0"],
    ["Sanchit", "COE", "2", "9.1"],
    ["Aditya", "IT", "2", "9.3"],
    ["Sagar", "SE", "1", "9.5"],
    ["Prateek", "MCE", "3", "7.8"],
]

filename = "student_records.csv"

# Writing to CSV file
with open(filename, mode="w", newline="", encoding="utf-8") as csvfile:
    csvwriter = csv.writer(csvfile)

    # Write header
    csvwriter.writerow(fields)

    # Write data rows
    csvwriter.writerows(rows)

print(f"Data successfully written to {filename}")