import re

txt = "Contact info: john@test.com, admin@domain.org, and user123@work.net"

# Finds all email-like structures
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"
results = re.findall(pattern, txt)

print("All matches:", results)