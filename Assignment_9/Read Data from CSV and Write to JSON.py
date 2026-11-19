import csv
import json

# Define file names
csv_file_path = "data.csv"
json_file_path = "output.json"


def csv_to_json(csv_path, json_path):
    data = []

    # Read CSV file and convert rows to dictionaries
    with open(csv_path, mode="r", encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    # Write data to JSON file
    with open(json_path, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)

    print(f"Successfully converted '{csv_path}' to '{json_path}'.")


# Example Execution
if __name__ == "__main__":
    # Sample run (Ensure 'data.csv' exists in your directory)
    try:
        csv_to_json(csv_file_path, json_file_path)
    except FileNotFoundError:
        print(f"Error: The file '{csv_file_path}' was not found.")