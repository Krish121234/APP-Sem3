import re

# Matching only 3-to-5 digit standalone numbers
text = "The room numbers are 101, 2045, and 123456 (ignore this), plus 9999."

pattern = r"\b\d{3,5}\b"
matches = re.findall(pattern, text)

print("Matched numbers:", matches)