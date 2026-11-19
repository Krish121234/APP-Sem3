import csv
import json

# ==============================================================================
# 1. READ DATA FROM CSV AND WRITE TO JSON (Core Aim of Experiment 9)
# ==============================================================================


def csv_to_json(csv_file_path, json_file_path):
    json_array = []

    # Read CSV file and convert each row to a dictionary
    with open(csv_file_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            json_array.append(row)

    # Write serialized JSON array to output file
    with open(json_file_path, mode="w", encoding="utf-8") as json_file:
        json_string = json.dumps(json_array, indent=4)
        json_file.write(json_string)

    print(f"[+] Successfully converted '{csv_file_path}' to '{json_file_path}'")


# ==============================================================================
# 2. CONVERT JSON TO CSV
# ==============================================================================


def json_to_csv(json_file_path, csv_file_path):
    with open(json_file_path, mode="r", encoding="utf-8") as json_file:
        json_data = json.load(json_file)

    with open(csv_file_path, mode="w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        count = 0

        for record in json_data:
            # Write header on first iteration
            if count == 0:
                header = record.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(record.values())

    print(f"[+] Successfully converted '{json_file_path}' to '{csv_file_path}'")


# ==============================================================================
# 3. READING CSV FILE USING csv.reader
# ==============================================================================


def read_csv_basic(file_path):
    fields = []
    rows = []

    with open(file_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.reader(csv_file)

        # Extract field names from the first row
        fields = next(csv_reader)

        # Extract remaining rows
        for row in csv_reader:
            rows.append(row)

        print(f"\n--- Reading {file_path} ---")
        print(f"Total number of rows: {csv_reader.line_num}")
        print("Field names are: " + ", ".join(fields))

        print("\nFirst 5 rows:")
        for row in rows[:5]:
            for col in row:
                print(col, end=" ")
            print()


# ==============================================================================
# 4. WRITING TO CSV FILE USING csv.writer & csv.DictWriter
# ==============================================================================


def write_csv_lists(file_path):
    fields = ["Name", "Branch", "Year", "CGPA"]
    rows = [
        ["Nikhil", "COE", "2", "9.0"],
        ["Sanchit", "COE", "2", "9.1"],
        ["Aditya", "IT", "2", "9.3"],
        ["Sagar", "SE", "1", "9.5"],
        ["Prateek", "MCE", "3", "7.8"],
        ["Sahil", "EP", "2", "9.1"],
    ]

    with open(file_path, mode="w", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(fields)
        csv_writer.writerows(rows)

    print(f"[+] Wrote list data to '{file_path}'")


def write_csv_dict(file_path):
    my_dict = [
        {"branch": "COE", "cgpa": "9.0", "name": "Nikhil", "year": "2"},
        {"branch": "COE", "cgpa": "9.1", "name": "Sanchit", "year": "2"},
        {"branch": "IT", "cgpa": "9.3", "name": "Aditya", "year": "2"},
        {"branch": "SE", "cgpa": "9.5", "name": "Sagar", "year": "1"},
        {"branch": "MCE", "cgpa": "7.8", "name": "Prateek", "year": "3"},
        {"branch": "EP", "cgpa": "9.1", "name": "Sahil", "year": "2"},
    ]
    fields = ["name", "branch", "year", "cgpa"]

    with open(file_path, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(my_dict)

    print(f"[+] Wrote dictionary data to '{file_path}'")


# ==============================================================================
# MAIN EXECUTION PIPELINE
# ==============================================================================

if __name__ == "__main__":
    # 1. Create a sample CSV file
    sample_csv = "data.csv"
    output_json = "data.json"
    reconverted_csv = "output.csv"

    # Write initial sample CSV
    with open(sample_csv, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["a", "b", "c"])
        writer.writerows(
            [
                ["25", "84", "com"],
                ["41", "52", "org"],
                ["58", "79", "io"],
                ["93", "21", "co"],
            ]
        )

    # 2. Run CSV to JSON conversion (Experiment 9 Main Task)
    csv_to_json(sample_csv, output_json)

    # 3. Read and print generated JSON
    with open(output_json, "r") as f:
        print("\nGenerated JSON Output:")
        print(f.read())

    # 4. Run JSON to CSV conversion
    json_to_csv(output_json, reconverted_csv)

    # 5. Execute basic reader/writer functions
    write_csv_lists("student_records.csv")
    write_csv_dict("university_records.csv")
    read_csv_basic("student_records.csv")