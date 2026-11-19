import json

# Sample Python Dictionary
student_data = {
    "name": "John",
    "age": 21,
    "course": "Computer Engineering",
    "subjects": ["Python", "DBMS", "OS"],
}

# 1. Writing Python dict to JSON file
json_filename = "student.json"
with open(json_filename, mode="w", encoding="utf-8") as json_file:
    json.dump(student_data, json_file, indent=4)

print(f"JSON data saved to {json_filename}")

# 2. Reading JSON file back to Python dict
with open(json_filename, mode="r", encoding="utf-8") as json_file:
    loaded_data = json.load(json_file)

print("\nData loaded from JSON file:")
print(loaded_data)