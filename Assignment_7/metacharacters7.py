import re

txt = "The rain in Spain"

# Pattern checks start (^) and end ($)
pattern = r"^The.*Spain$"
match = re.search(pattern, txt)

if match:
    print("Match found:", match.group())
else:
    print("No match found.")