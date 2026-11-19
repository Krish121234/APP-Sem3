import re

txt = "Order #12345 was placed by customer@store.com on Monday."

# Search for the first email
pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}"
match = re.search(pattern, txt)

if match:
    print("First match:", match.group())
    print("Start index:", match.start())
    print("End index:", match.end())